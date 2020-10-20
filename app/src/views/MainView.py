# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainView.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class MainView(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(30, 20, 177, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.main_text = QtWidgets.QLabel(self.centralwidget)
        self.main_text.setGeometry(QtCore.QRect(380, 90, 67, 17))
        self.main_text.setObjectName("main_text")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 330, 141, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 330, 141, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(470, 330, 161, 17))
        self.label_3.setObjectName("label_3")
        self.trening_this_week = QtWidgets.QLabel(self.centralwidget)
        self.trening_this_week.setGeometry(QtCore.QRect(360, 370, 67, 17))
        self.trening_this_week.setObjectName("trening_this_week")
        self.trening_today = QtWidgets.QLabel(self.centralwidget)
        self.trening_today.setGeometry(QtCore.QRect(230, 370, 67, 17))
        self.trening_today.setObjectName("trening_today")
        self.trening_this_month = QtWidgets.QLabel(self.centralwidget)
        self.trening_this_month.setGeometry(QtCore.QRect(500, 370, 67, 17))
        self.trening_this_month.setObjectName("trening_this_month")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow, ):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.commandLinkButton.setText(_translate("MainWindow", "CommandLinkButton"))
        self.main_text.setText(_translate("MainWindow", "Hellp"))
        self.label.setText(_translate("MainWindow", "trenings today"))
        self.label_2.setText(_translate("MainWindow", "trenings this week"))
        self.label_3.setText(_translate("MainWindow", "trenings this month"))
        self.trening_this_week.setText(_translate("MainWindow", "TextLabel"))
        self.trening_today.setText(_translate("MainWindow", "TextLabel"))
        self.trening_this_month.setText(_translate("MainWindow", "TextLabel"))