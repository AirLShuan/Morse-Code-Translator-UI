# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'translator_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MorseCode(object):
    def setupUi(self, MorseCode):
        if not MorseCode.objectName():
            MorseCode.setObjectName(u"MorseCode")
        MorseCode.resize(800, 335)
        MorseCode.setStyleSheet(u"QMainWindow {\n"
"	background-color: rgb(49, 49, 49);\n"
"}\n"
"\n"
"QWidget {\n"
"	background-color: rgb(49, 49, 49);\n"
"}")
        self.centralwidget = QWidget(MorseCode)
        self.centralwidget.setObjectName(u"centralwidget")
        self.output = QLabel(self.centralwidget)
        self.output.setObjectName(u"output")
        self.output.setGeometry(QRect(70, 110, 651, 71))
        font = QFont()
        font.setPointSize(16)
        self.output.setFont(font)
        self.output.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(102, 102, 102);\n"
"	padding-right: 10px;\n"
"	padding-left: 10px;\n"
"}")
        self.output.setFrameShape(QFrame.Panel)
        self.output.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(80, 30, 631, 41))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setUnderline(True)
        font1.setWeight(75)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.title.setFont(font1)
        self.title.setFrameShape(QFrame.StyledPanel)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setTextInteractionFlags(Qt.NoTextInteraction)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(90, 200, 611, 61))
        self.input_bttns = QHBoxLayout(self.layoutWidget)
        self.input_bttns.setObjectName(u"input_bttns")
        self.input_bttns.setContentsMargins(0, 0, 0, 0)
        self.pushButton_dash = QPushButton(self.layoutWidget)
        self.pushButton_dash.setObjectName(u"pushButton_dash")
        font2 = QFont()
        font2.setPointSize(12)
        self.pushButton_dash.setFont(font2)
        self.pushButton_dash.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(102, 102, 102)\n"
"}")

        self.input_bttns.addWidget(self.pushButton_dash)

        self.pushButton_dot = QPushButton(self.layoutWidget)
        self.pushButton_dot.setObjectName(u"pushButton_dot")
        self.pushButton_dot.setFont(font2)
        self.pushButton_dot.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(102, 102, 102)\n"
"}")

        self.input_bttns.addWidget(self.pushButton_dot)

        self.pushButton_space = QPushButton(self.layoutWidget)
        self.pushButton_space.setObjectName(u"pushButton_space")
        self.pushButton_space.setFont(font2)
        self.pushButton_space.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(102, 102, 102)\n"
"}")

        self.input_bttns.addWidget(self.pushButton_space)

        self.pushButton_enter = QPushButton(self.layoutWidget)
        self.pushButton_enter.setObjectName(u"pushButton_enter")
        self.pushButton_enter.setFont(font2)
        self.pushButton_enter.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(102, 102, 102)\n"
"}")

        self.input_bttns.addWidget(self.pushButton_enter)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(260, 270, 281, 35))
        self.remove_bttns = QHBoxLayout(self.layoutWidget1)
        self.remove_bttns.setObjectName(u"remove_bttns")
        self.remove_bttns.setContentsMargins(0, 0, 0, 0)
        self.pushButton_backspace = QPushButton(self.layoutWidget1)
        self.pushButton_backspace.setObjectName(u"pushButton_backspace")
        self.pushButton_backspace.setFont(font2)
        self.pushButton_backspace.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(102, 102, 102)\n"
"}")

        self.remove_bttns.addWidget(self.pushButton_backspace)

        self.pushButton_clear = QPushButton(self.layoutWidget1)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        self.pushButton_clear.setFont(font2)
        self.pushButton_clear.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(102, 102, 102)\n"
"}")

        self.remove_bttns.addWidget(self.pushButton_clear)

        MorseCode.setCentralWidget(self.centralwidget)

        self.retranslateUi(MorseCode)

        QMetaObject.connectSlotsByName(MorseCode)
    # setupUi

    def retranslateUi(self, MorseCode):
        MorseCode.setWindowTitle(QCoreApplication.translate("MorseCode", u"Morse Code Translater", None))
#if QT_CONFIG(accessibility)
        MorseCode.setAccessibleName(QCoreApplication.translate("MorseCode", u"MorseDecoder", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        MorseCode.setAccessibleDescription(QCoreApplication.translate("MorseCode", u"Takes Morse Code & Turns it into English", None))
#endif // QT_CONFIG(accessibility)
        self.output.setText("")
        self.title.setText(QCoreApplication.translate("MorseCode", u"<html><head/><body><p><span style=\" color:#fdfdfd;\">Morse Code Translator</span></p></body></html>", None))
        self.pushButton_dash.setText(QCoreApplication.translate("MorseCode", u"-", None))
        self.pushButton_dot.setText(QCoreApplication.translate("MorseCode", u".", None))
        self.pushButton_space.setText(QCoreApplication.translate("MorseCode", u"space", None))
        self.pushButton_enter.setText(QCoreApplication.translate("MorseCode", u"enter", None))
        self.pushButton_backspace.setText(QCoreApplication.translate("MorseCode", u"backspace", None))
        self.pushButton_clear.setText(QCoreApplication.translate("MorseCode", u"clear", None))
    # retranslateUi

