# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/MainView.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.page_main = QtWidgets.QStackedWidget(self.centralwidget)
        self.page_main.setGeometry(QtCore.QRect(140, 0, 631, 561))
        self.page_main.setObjectName("page_main")
        self.view_main = QtWidgets.QWidget()
        self.view_main.setObjectName("view_main")
        self.trening_today = QtWidgets.QLabel(self.view_main)
        self.trening_today.setGeometry(QtCore.QRect(80, 340, 67, 17))
        self.trening_today.setObjectName("trening_today")
        self.label_3 = QtWidgets.QLabel(self.view_main)
        self.label_3.setGeometry(QtCore.QRect(360, 290, 161, 17))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.view_main)
        self.label_2.setGeometry(QtCore.QRect(190, 290, 141, 17))
        self.label_2.setObjectName("label_2")
        self.trening_this_week = QtWidgets.QLabel(self.view_main)
        self.trening_this_week.setGeometry(QtCore.QRect(210, 330, 67, 17))
        self.trening_this_week.setObjectName("trening_this_week")
        self.trening_this_month = QtWidgets.QLabel(self.view_main)
        self.trening_this_month.setGeometry(QtCore.QRect(380, 340, 67, 17))
        self.trening_this_month.setObjectName("trening_this_month")
        self.main_text = QtWidgets.QLabel(self.view_main)
        self.main_text.setGeometry(QtCore.QRect(260, 50, 67, 17))
        self.main_text.setObjectName("main_text")
        self.label = QtWidgets.QLabel(self.view_main)
        self.label.setGeometry(QtCore.QRect(60, 290, 141, 17))
        self.label.setObjectName("label")
        self.page_main.addWidget(self.view_main)
        self.view_settings = QtWidgets.QWidget()
        self.view_settings.setObjectName("view_settings")
        self.label_4 = QtWidgets.QLabel(self.view_settings)
        self.label_4.setGeometry(QtCore.QRect(280, 70, 67, 17))
        self.label_4.setObjectName("label_4")
        self.page_main.addWidget(self.view_settings)
        self.nav_main = QtWidgets.QPushButton(self.centralwidget)
        self.nav_main.setGeometry(QtCore.QRect(10, 10, 89, 25))
        self.nav_main.setObjectName("nav_main")
        self.nav_settings = QtWidgets.QPushButton(self.centralwidget)
        self.nav_settings.setGeometry(QtCore.QRect(0, 60, 89, 25))
        self.nav_settings.setObjectName("nav_settings")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.page_main.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.trening_today.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "trenings this month"))
        self.label_2.setText(_translate("MainWindow", "trenings this week"))
        self.trening_this_week.setText(_translate("MainWindow", "TextLabel"))
        self.trening_this_month.setText(_translate("MainWindow", "TextLabel"))
        self.main_text.setText(_translate("MainWindow", "Hellp"))
        self.label.setText(_translate("MainWindow", "trenings today"))
        self.label_4.setText(_translate("MainWindow", "Settings"))
        self.nav_main.setText(_translate("MainWindow", "Homepage"))
        self.nav_settings.setText(_translate("MainWindow", "Settings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
