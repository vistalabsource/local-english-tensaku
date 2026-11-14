# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QStatusBar, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(720, 540)
        MainWindow.setMinimumSize(QSize(720, 540))
        MainWindow.setMaximumSize(QSize(720, 540))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.english_text = QPlainTextEdit(self.centralwidget)
        self.english_text.setObjectName(u"english_text")

        self.verticalLayout_2.addWidget(self.english_text)

        self.start_fix = QPushButton(self.centralwidget)
        self.start_fix.setObjectName(u"start_fix")

        self.verticalLayout_2.addWidget(self.start_fix)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.result = QTextBrowser(self.centralwidget)
        self.result.setObjectName(u"result")

        self.verticalLayout.addWidget(self.result)

        self.why = QTextBrowser(self.centralwidget)
        self.why.setObjectName(u"why")

        self.verticalLayout.addWidget(self.why)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 720, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.english_text.setPlainText(QCoreApplication.translate("MainWindow", u"Please enter to English text here.", None))
        self.start_fix.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u524a", None))
        self.result.setMarkdown(QCoreApplication.translate("MainWindow", u"\u6dfb\u524a\u7d50\u679c\u304c\u3053\u3053\u306b\u8868\u793a\u3055\u308c\u307e\u3059\u3002\n"
"\n"
"", None))
        self.why.setMarkdown(QCoreApplication.translate("MainWindow", u"\u7406\u7531\u304c\u3053\u3053\u306b\u8868\u793a\u3055\u308c\u307e\u3059\u3002\n"
"\n"
"", None))
    # retranslateUi

