# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'my_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 335)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"	background-color: rgb(49, 49, 49);\n"
"}\n"
"\n"
"QWidget {\n"
"	background-color: rgb(49, 49, 49);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
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
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(90, 200, 611, 61))
        self.input_bttns = QHBoxLayout(self.widget)
        self.input_bttns.setObjectName(u"input_bttns")
        self.input_bttns.setContentsMargins(0, 0, 0, 0)
        self.dash_bttn = QPushButton(self.widget)
        self.dash_bttn.setObjectName(u"dash_bttn")
        font2 = QFont()
        font2.setPointSize(12)
        self.dash_bttn.setFont(font2)
        self.dash_bttn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(102, 102, 102)\n"
"}")

        self.input_bttns.addWidget(self.dash_bttn)

        self.dot_bttn = QPushButton(self.widget)
        self.dot_bttn.setObjectName(u"dot_bttn")
        self.dot_bttn.setFont(font2)
        self.dot_bttn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(102, 102, 102)\n"
"}")

        self.input_bttns.addWidget(self.dot_bttn)

        self.space_bttn = QPushButton(self.widget)
        self.space_bttn.setObjectName(u"space_bttn")
        self.space_bttn.setFont(font2)
        self.space_bttn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(102, 102, 102)\n"
"}")

        self.input_bttns.addWidget(self.space_bttn)

        self.enter_bttn = QPushButton(self.widget)
        self.enter_bttn.setObjectName(u"enter_bttn")
        self.enter_bttn.setFont(font2)
        self.enter_bttn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(102, 102, 102)\n"
"}")

        self.input_bttns.addWidget(self.enter_bttn)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(260, 270, 281, 35))
        self.remove_bttns = QHBoxLayout(self.widget1)
        self.remove_bttns.setObjectName(u"remove_bttns")
        self.remove_bttns.setContentsMargins(0, 0, 0, 0)
        self.clear_bttn = QPushButton(self.widget1)
        self.clear_bttn.setObjectName(u"clear_bttn")
        self.clear_bttn.setFont(font2)
        self.clear_bttn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(102, 102, 102)\n"
"}")

        self.remove_bttns.addWidget(self.clear_bttn)

        self.del_bttn = QPushButton(self.widget1)
        self.del_bttn.setObjectName(u"del_bttn")
        self.del_bttn.setFont(font2)
        self.del_bttn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(102, 102, 102)\n"
"}")

        self.remove_bttns.addWidget(self.del_bttn)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.output.setText("")
        self.title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#fdfdfd;\">Morse Code Translator</span></p></body></html>", None))
        self.dash_bttn.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.dot_bttn.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.space_bttn.setText(QCoreApplication.translate("MainWindow", u"space", None))
        self.enter_bttn.setText(QCoreApplication.translate("MainWindow", u"enter", None))
        self.clear_bttn.setText(QCoreApplication.translate("MainWindow", u"clear", None))
        self.del_bttn.setText(QCoreApplication.translate("MainWindow", u"backspace", None))
    # retranslateUi

