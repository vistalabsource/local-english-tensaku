from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from GUI import Ui_MainWindow

import json
import sys
from threading import Event

import ollama


class TextFixThread(QThread):
    result_ready = Signal(str, str)
    error_occurred = Signal(str)
    model_missing = Signal()

    def __init__(self, prompt, input_text, parent=None):
        super().__init__(parent)
        self.prompt = prompt
        self.input_text = input_text
        self._install_decision = Event()
        self._install_model = False

    def allow_model_install(self, allow):
        self._install_model = allow
        self._install_decision.set()

    def run(self):
        model = "gemma4:e4b"
        try:
            try:
                ollama.show(model)
            except ollama.ResponseError as error:
                error_message = error.error.lower()
                if (
                    error.status_code != 404
                    or model.lower() not in error_message
                    or "not found" not in error_message
                ):
                    raise
                self.model_missing.emit()
                self._install_decision.wait()
                if not self._install_model:
                    return
                ollama.pull(model)

            response = ollama.chat(
                model=model,
                messages=[
                    {"role": "user", "content": self.prompt + self.input_text}
                ],
                format="json",
            )
            result = json.loads(response['message']['content'])
            self.result_ready.emit(result["corrected_text"], result["explanation"])
        except Exception as error:
            self.error_occurred.emit(str(error))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("ローカル英語添削ツール version 1.0")
        self.text_fix_thread = None

        self.ui.start_fix.clicked.connect(self.fix_text)

        self.show()

    def fix_text(self):
        prompt = """
        以下の文章を文法的に正しい英語に修正してください。
        修正後の英文と、主な修正理由を日本語で説明してください。
        次のキーを持つJSONオブジェクトだけを出力してください:
        - "corrected_text": 修正後の英文
        - "explanation": 修正した理由の日本語説明
        """

        input_text = self.ui.english_text.toPlainText()
        self.ui.start_fix.setEnabled(False)
        self.statusBar().showMessage("添削中... しばらくお待ちください。")
        self.text_fix_thread = TextFixThread(prompt, input_text, self)
        self.text_fix_thread.result_ready.connect(self._display_result)
        self.text_fix_thread.error_occurred.connect(self._show_error)
        self.text_fix_thread.model_missing.connect(self._confirm_model_install)
        self.text_fix_thread.finished.connect(self._on_text_fix_finished)
        self.text_fix_thread.start()

    def _confirm_model_install(self):
        answer = QMessageBox.question(
            self,
            "モデルのインストール",
            "必要なモデル「Gemma 4 E4B」がインストールされていません。インストールしますか？\n（約5GB、Ollamaが必要です）",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        allow_install = answer == QMessageBox.Yes
        if allow_install:
            self.statusBar().showMessage("モデルをインストールしています...")
        self.text_fix_thread.allow_model_install(allow_install)

    def _show_error(self, error):
        self.statusBar().clearMessage()
        QMessageBox.critical(self, "エラー", f"処理に失敗しました: {error}")

    def _display_result(self, corrected_text, explanation):
        self.statusBar().clearMessage()
        self.ui.result.setPlainText(corrected_text)
        self.ui.why.setMarkdown(explanation)

    def _on_text_fix_finished(self):
        self.ui.start_fix.setEnabled(True)
        self.text_fix_thread.deleteLater()
        self.text_fix_thread = None
        self.statusBar().clearMessage()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())