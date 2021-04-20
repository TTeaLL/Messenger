# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'messenger.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(560, 529)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.messagesBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.messagesBrowser.setGeometry(QtCore.QRect(30, 60, 521, 371))
        self.messagesBrowser.setObjectName("messagesBrowser")
        self.textInput = QtWidgets.QTextEdit(self.centralwidget)
        self.textInput.setGeometry(QtCore.QRect(30, 440, 481, 31))
        self.textInput.setObjectName("textInput")
        self.sendButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendButton.setGeometry(QtCore.QRect(520, 440, 31, 31))
        self.sendButton.setObjectName("sendButton")
        self.nameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.nameInput.setGeometry(QtCore.QRect(430, 30, 113, 22))
        self.nameInput.setObjectName("nameInput")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 30, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 560, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Messenger"))
        self.label.setText(_translate("MainWindow", "Messenger"))
        self.textInput.setPlaceholderText(_translate("MainWindow", "Введите сообщение..."))
        self.sendButton.setText(_translate("MainWindow", ">"))
        self.nameInput.setPlaceholderText(_translate("MainWindow", "Имя"))
        self.label_2.setText(_translate("MainWindow", "Name:"))
