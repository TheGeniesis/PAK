# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainView.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import ui.appimages

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1108, 769)
        MainWindow.setStyleSheet("background: none;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.page_main = QtWidgets.QStackedWidget(self.centralwidget)
        self.page_main.setGeometry(QtCore.QRect(50, 90, 1001, 611))
        self.page_main.setAutoFillBackground(False)
        self.page_main.setStyleSheet("border-style: outset;\n"
"background-color: rgb(255, 255, 255);\n"
"border-width: 1px;\n"
"border-radius: 20px;\n"
"border-color: black;\n"
"font: bold14px;")
        self.page_main.setObjectName("page_main")
        self.view_main = QtWidgets.QWidget()
        self.view_main.setObjectName("view_main")
        self.main_training_today = QtWidgets.QLabel(self.view_main)
        self.main_training_today.setGeometry(QtCore.QRect(360, 220, 67, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe WP")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.main_training_today.setFont(font)
        self.main_training_today.setStyleSheet("border: none;\n"
"background: transparent;")
        self.main_training_today.setObjectName("main_training_today")
        self.label_3 = QtWidgets.QLabel(self.view_main)
        self.label_3.setGeometry(QtCore.QRect(780, 120, 191, 71))
        self.label_3.setStyleSheet("image: url(:/trainingmonth/png/Done exercises this month.png);\n"
"\n"
"\n"
"border: none;\n"
"background: transparent;\n"
"font: bold14px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.view_main)
        self.label_2.setGeometry(QtCore.QRect(540, 120, 191, 71))
        self.label_2.setStyleSheet("image: url(:/traningweek/png/Done exercises this week.png);\n"
"\n"
"border: none;\n"
"background: transparent;\n"
"font: bold14px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.main_training_this_week = QtWidgets.QLabel(self.view_main)
        self.main_training_this_week.setGeometry(QtCore.QRect(620, 210, 67, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe WP")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.main_training_this_week.setFont(font)
        self.main_training_this_week.setStyleSheet("border: none;\n"
"background: transparent;")
        self.main_training_this_week.setObjectName("main_training_this_week")
        self.main_training_this_month = QtWidgets.QLabel(self.view_main)
        self.main_training_this_month.setGeometry(QtCore.QRect(840, 220, 67, 17))
        font = QtGui.QFont()
        font.setFamily("Segoe WP")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.main_training_this_month.setFont(font)
        self.main_training_this_month.setStyleSheet("border: none;\n"
"background: transparent;")
        self.main_training_this_month.setObjectName("main_training_this_month")
        self.main_text = QtWidgets.QLabel(self.view_main)
        self.main_text.setEnabled(False)
        self.main_text.setGeometry(QtCore.QRect(410, 30, 321, 51))
        self.main_text.setStyleSheet("image: url(:/hello/png/Hello there!.png);\n"
"background: transparent;\n"
"border-style: transparent;\n"
"border: none;")
        self.main_text.setText("")
        self.main_text.setObjectName("main_text")
        self.label = QtWidgets.QLabel(self.view_main)
        self.label.setGeometry(QtCore.QRect(290, 120, 191, 71))
        self.label.setStyleSheet("image: url(:/treningtoday/png/Done exercises today.png);\n"
"\n"
"border: none;\n"
"background: transparent;\n"
"font: bold14px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.page_main.addWidget(self.view_main)
        self.view_video = QtWidgets.QWidget()
        self.view_video.setObjectName("view_video")
        self.label_5 = QtWidgets.QLabel(self.view_video)
        self.label_5.setGeometry(QtCore.QRect(420, 420, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe WP")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border: none;\n"
"background: transparent;")
        self.label_5.setObjectName("label_5")
        self.b_video_exercise_yes = QtWidgets.QPushButton(self.view_video)
        self.b_video_exercise_yes.setGeometry(QtCore.QRect(470, 470, 91, 25))
        self.b_video_exercise_yes.setStyleSheet("border: none;\n"
"background: transparent;")
        self.b_video_exercise_yes.setObjectName("b_video_exercise_yes")
        self.b_video_exercise_no = QtWidgets.QPushButton(self.view_video)
        self.b_video_exercise_no.setGeometry(QtCore.QRect(610, 470, 89, 25))
        self.b_video_exercise_no.setStyleSheet("border: none;\n"
"background: transparent;")
        self.b_video_exercise_no.setObjectName("b_video_exercise_no")
        self.video_widget = QtWidgets.QWidget(self.view_video)
        self.video_widget.setGeometry(QtCore.QRect(230, 40, 691, 351))
        self.video_widget.setStyleSheet("border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;")
        self.video_widget.setObjectName("video_widget")
        self.f_video_length = QtWidgets.QSlider(self.video_widget)
        self.f_video_length.setGeometry(QtCore.QRect(40, 320, 201, 16))
        self.f_video_length.setStyleSheet("border: none;")
        self.f_video_length.setOrientation(QtCore.Qt.Horizontal)
        self.f_video_length.setObjectName("f_video_length")
        self.video_box = QtWidgets.QWidget(self.video_widget)
        self.video_box.setGeometry(QtCore.QRect(50, 30, 601, 221))
        self.video_box.setStyleSheet("border-width: 2px;\n"
"border-radius: 0px;")
        self.video_box.setObjectName("video_box")
        self.video_id = QtWidgets.QLabel(self.video_box)
        self.video_id.setGeometry(QtCore.QRect(180, 40, 51, 17))
        self.video_id.setStyleSheet("border: none;")
        self.video_id.setObjectName("video_id")
        self.video_media_player = QtWidgets.QWidget(self.video_box)
        self.video_media_player.setGeometry(QtCore.QRect(10, 20, 120, 80))
        self.video_media_player.setStyleSheet("border: none;")
        self.video_media_player.setObjectName("video_media_player")
        self.b_video_play = QtWidgets.QPushButton(self.video_widget)
        self.b_video_play.setGeometry(QtCore.QRect(40, 260, 41, 41))
        self.b_video_play.setStyleSheet("image: url(:/playbutton/png/play.jpg);\n"
"border-width: 2px;\n"
"border-radius: 0px;")
        self.b_video_play.setText("")
        self.b_video_play.setObjectName("b_video_play")
        self.nav_settings_2 = QtWidgets.QPushButton(self.view_video)
        self.nav_settings_2.setGeometry(QtCore.QRect(990, 100, 131, 51))
        self.nav_settings_2.setMaximumSize(QtCore.QSize(131, 300))
        self.nav_settings_2.setStyleSheet("\n"
"border: none;\n"
"background: transparent;\n"
"font: bold14px;\n"
"image: url(:/Settings/png/Settings.png);")
        self.nav_settings_2.setText("")
        self.nav_settings_2.setObjectName("nav_settings_2")
        self.nav_video_2 = QtWidgets.QPushButton(self.view_video)
        self.nav_video_2.setGeometry(QtCore.QRect(990, 180, 131, 51))
        self.nav_video_2.setMaximumSize(QtCore.QSize(131, 300))
        self.nav_video_2.setStyleSheet("image: url(:/Video/png/video2.png);\n"
"border: none;\n"
"background: transparent;\n"
"font: bold14px;")
        self.nav_video_2.setText("")
        self.nav_video_2.setObjectName("nav_video_2")
        self.nav_main_2 = QtWidgets.QPushButton(self.view_video)
        self.nav_main_2.setGeometry(QtCore.QRect(990, 10, 131, 51))
        self.nav_main_2.setMaximumSize(QtCore.QSize(131, 300))
        self.nav_main_2.setStyleSheet("image: url(:/Main/png/home2.png);\n"
"font: bold14px;\n"
"border: none;\n"
"background: transparent;")
        self.nav_main_2.setText("")
        self.nav_main_2.setObjectName("nav_main_2")
        self.nav_summary_2 = QtWidgets.QPushButton(self.view_video)
        self.nav_summary_2.setGeometry(QtCore.QRect(990, 260, 131, 51))
        self.nav_summary_2.setStyleSheet("image: url(:/Summary/png/summary2.png);\n"
"font: bold14px;\n"
"border: none;\n"
"background: transparent;")
        self.nav_summary_2.setText("")
        self.nav_summary_2.setObjectName("nav_summary_2")
        self.page_main.addWidget(self.view_video)
        self.view_exercise_declined = QtWidgets.QWidget()
        self.view_exercise_declined.setObjectName("view_exercise_declined")
        self.label_7 = QtWidgets.QLabel(self.view_exercise_declined)
        self.label_7.setGeometry(QtCore.QRect(300, 170, 611, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe WP")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border: none;\n"
"background: transparent;")
        self.label_7.setObjectName("label_7")
        self.f_exercise_declined_comment = QtWidgets.QPlainTextEdit(self.view_exercise_declined)
        self.f_exercise_declined_comment.setGeometry(QtCore.QRect(300, 220, 611, 181))
        self.f_exercise_declined_comment.setStyleSheet("border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.f_exercise_declined_comment.setObjectName("f_exercise_declined_comment")
        self.b_exercise_declined_confirm = QtWidgets.QPushButton(self.view_exercise_declined)
        self.b_exercise_declined_confirm.setGeometry(QtCore.QRect(560, 430, 91, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe WP")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.b_exercise_declined_confirm.setFont(font)
        self.b_exercise_declined_confirm.setStyleSheet("border: none;\n"
"background: transparent;")
        self.b_exercise_declined_confirm.setObjectName("b_exercise_declined_confirm")
        self.page_main.addWidget(self.view_exercise_declined)
        self.view_exercise_grade = QtWidgets.QWidget()
        self.view_exercise_grade.setObjectName("view_exercise_grade")
        self.b_exercise_grade_1 = QtWidgets.QPushButton(self.view_exercise_grade)
        self.b_exercise_grade_1.setGeometry(QtCore.QRect(310, 310, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe WP")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.b_exercise_grade_1.setFont(font)
        self.b_exercise_grade_1.setStyleSheet("image: url(:/faces/png/dissapointed.png);\n"
"background: transparent;\n"
"border: none;")
        self.b_exercise_grade_1.setText("")
        self.b_exercise_grade_1.setObjectName("b_exercise_grade_1")
        self.b_exercise_grade_2 = QtWidgets.QPushButton(self.view_exercise_grade)
        self.b_exercise_grade_2.setGeometry(QtCore.QRect(445, 310, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe WP")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.b_exercise_grade_2.setFont(font)
        self.b_exercise_grade_2.setStyleSheet("image: url(:/faces/png/sad.png);\n"
"background: transparent;\n"
"border: none;")
        self.b_exercise_grade_2.setText("")
        self.b_exercise_grade_2.setObjectName("b_exercise_grade_2")
        self.b_exercise_grade_3 = QtWidgets.QPushButton(self.view_exercise_grade)
        self.b_exercise_grade_3.setGeometry(QtCore.QRect(585, 310, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe WP")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.b_exercise_grade_3.setFont(font)
        self.b_exercise_grade_3.setStyleSheet("image: url(:/faces/png/surprised.png);\n"
"background: transparent;\n"
"border: none;")
        self.b_exercise_grade_3.setText("")
        self.b_exercise_grade_3.setObjectName("b_exercise_grade_3")
        self.b_exercise_grade_4 = QtWidgets.QPushButton(self.view_exercise_grade)
        self.b_exercise_grade_4.setGeometry(QtCore.QRect(725, 310, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe WP")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.b_exercise_grade_4.setFont(font)
        self.b_exercise_grade_4.setStyleSheet("image: url(:/faces/png/smiling.png);\n"
"background: transparent;\n"
"border: none;")
        self.b_exercise_grade_4.setText("")
        self.b_exercise_grade_4.setObjectName("b_exercise_grade_4")
        self.b_exercise_grade_5 = QtWidgets.QPushButton(self.view_exercise_grade)
        self.b_exercise_grade_5.setGeometry(QtCore.QRect(860, 310, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe WP")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.b_exercise_grade_5.setFont(font)
        self.b_exercise_grade_5.setStyleSheet("image: url(:/faces/png/happy.png);\n"
"background: transparent;\n"
"border: none;")
        self.b_exercise_grade_5.setText("")
        self.b_exercise_grade_5.setObjectName("b_exercise_grade_5")
        self.label_8 = QtWidgets.QLabel(self.view_exercise_grade)
        self.label_8.setGeometry(QtCore.QRect(280, 90, 621, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe WP")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("border: none;\n"
"background: transparent;")
        self.label_8.setObjectName("label_8")
        self.page_main.addWidget(self.view_exercise_grade)
        self.view_settings = QtWidgets.QWidget()
        self.view_settings.setObjectName("view_settings")
        self.label_4 = QtWidgets.QLabel(self.view_settings)
        self.label_4.setGeometry(QtCore.QRect(360, 30, 321, 51))
        self.label_4.setStyleSheet("image: url(:/Settings/png/Settings.png);\n"
"border: none;\n"
"background: transparent;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_9 = QtWidgets.QLabel(self.view_settings)
        self.label_9.setGeometry(QtCore.QRect(410, 90, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe WP")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("border: none;\n"
"background: transparent;")
        self.label_9.setObjectName("label_9")
        self.f_settings_check_absence = QtWidgets.QCheckBox(self.view_settings)
        self.f_settings_check_absence.setGeometry(QtCore.QRect(390, 180, 241, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe WP")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.f_settings_check_absence.setFont(font)
        self.f_settings_check_absence.setStyleSheet("border: none;\n"
"background: transparent;")
        self.f_settings_check_absence.setObjectName("f_settings_check_absence")
        self.f_settings_start_with_os = QtWidgets.QCheckBox(self.view_settings)
        self.f_settings_start_with_os.setGeometry(QtCore.QRect(390, 230, 241, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe WP")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.f_settings_start_with_os.setFont(font)
        self.f_settings_start_with_os.setStyleSheet("border: none;\n"
"background: transparent;")
        self.f_settings_start_with_os.setObjectName("f_settings_start_with_os")
        self.b_settings_confirm = QtWidgets.QPushButton(self.view_settings)
        self.b_settings_confirm.setGeometry(QtCore.QRect(470, 330, 89, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe WP")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.b_settings_confirm.setFont(font)
        self.b_settings_confirm.setStyleSheet("border: none;\n"
"background: transparent;")
        self.b_settings_confirm.setObjectName("b_settings_confirm")
        self.f_settings_exercise_interval = QtWidgets.QSlider(self.view_settings)
        self.f_settings_exercise_interval.setGeometry(QtCore.QRect(420, 130, 201, 16))
        self.f_settings_exercise_interval.setStyleSheet("border: none;")
        self.f_settings_exercise_interval.setOrientation(QtCore.Qt.Horizontal)
        self.f_settings_exercise_interval.setObjectName("f_settings_exercise_interval")
        self.page_main.addWidget(self.view_settings)
        self.view_summary = QtWidgets.QWidget()
        self.view_summary.setObjectName("view_summary")
        self.label_6 = QtWidgets.QLabel(self.view_summary)
        self.label_6.setGeometry(QtCore.QRect(400, 30, 321, 51))
        self.label_6.setStyleSheet("image: url(:/Summary/png/summary.png);\n"
"border: none;\n"
"background: transparent;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.summary_calendar = QtWidgets.QCalendarWidget(self.view_summary)
        self.summary_calendar.setGeometry(QtCore.QRect(330, 100, 491, 311))
        font = QtGui.QFont()
        font.setFamily("Segoe WP")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.summary_calendar.setFont(font)
        self.summary_calendar.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-width: 1px;\n"
"border-radius: 3px;\n"
"border-color: black;")
        self.summary_calendar.setObjectName("summary_calendar")
        self.label_10 = QtWidgets.QLabel(self.view_summary)
        self.label_10.setGeometry(QtCore.QRect(330, 420, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe WP")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("border: none;\n"
"background: transparent;")
        self.label_10.setObjectName("label_10")
        self.summary_exercises_amount = QtWidgets.QLabel(self.view_summary)
        self.summary_exercises_amount.setGeometry(QtCore.QRect(450, 430, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe WP")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.summary_exercises_amount.setFont(font)
        self.summary_exercises_amount.setStyleSheet("border: none;\n"
"background: transparent;")
        self.summary_exercises_amount.setObjectName("summary_exercises_amount")
        self.page_main.addWidget(self.view_summary)
        self.nav_summary = QtWidgets.QPushButton(self.centralwidget)
        self.nav_summary.setGeometry(QtCore.QRect(70, 430, 131, 51))
        self.nav_summary.setStyleSheet("image: url(:/Summary/png/summary2.png);\n"
"font: bold14px;\n"
"border: none;\n"
"background: transparent;")
        self.nav_summary.setText("")
        self.nav_summary.setObjectName("nav_summary")
        self.nav_video = QtWidgets.QPushButton(self.centralwidget)
        self.nav_video.setGeometry(QtCore.QRect(70, 350, 131, 51))
        self.nav_video.setMaximumSize(QtCore.QSize(131, 300))
        self.nav_video.setStyleSheet("image: url(:/Video/png/video2.png);\n"
"border: none;\n"
"background: transparent;\n"
"font: bold14px;")
        self.nav_video.setText("")
        self.nav_video.setObjectName("nav_video")
        self.nav_main = QtWidgets.QPushButton(self.centralwidget)
        self.nav_main.setGeometry(QtCore.QRect(70, 180, 131, 51))
        self.nav_main.setMaximumSize(QtCore.QSize(131, 300))
        self.nav_main.setStyleSheet("image: url(:/Main/png/home2.png);\n"
"font: bold14px;\n"
"border: none;\n"
"background: transparent;")
        self.nav_main.setText("")
        self.nav_main.setObjectName("nav_main")
        self.nav_settings = QtWidgets.QPushButton(self.centralwidget)
        self.nav_settings.setGeometry(QtCore.QRect(70, 270, 131, 51))
        self.nav_settings.setMaximumSize(QtCore.QSize(131, 300))
        self.nav_settings.setStyleSheet("\n"
"border: none;\n"
"background: transparent;\n"
"font: bold14px;\n"
"image: url(:/Settings/png/Settings.png);")
        self.nav_settings.setText("")
        self.nav_settings.setObjectName("nav_settings")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.page_main.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main_training_today.setText(_translate("MainWindow", "TextLabel"))
        self.main_training_this_week.setText(_translate("MainWindow", "TextLabel"))
        self.main_training_this_month.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "     Do you want to do the exercises now?"))
        self.b_video_exercise_yes.setText(_translate("MainWindow", "Yes"))
        self.b_video_exercise_no.setText(_translate("MainWindow", "No"))
        self.video_id.setText(_translate("MainWindow", "1"))
        self.label_7.setText(_translate("MainWindow", "                                                Why did you decline exercieses?"))
        self.b_exercise_declined_confirm.setText(_translate("MainWindow", "Confirm"))
        self.label_8.setText(_translate("MainWindow", "                   Grade exercise"))
        self.label_9.setText(_translate("MainWindow", "Exercise interval"))
        self.f_settings_check_absence.setText(_translate("MainWindow", "Check absence"))
        self.f_settings_start_with_os.setText(_translate("MainWindow", "Start with system"))
        self.b_settings_confirm.setText(_translate("MainWindow", "Confirm"))
        self.label_10.setText(_translate("MainWindow", "       Exercises:"))
        self.summary_exercises_amount.setText(_translate("MainWindow", "0"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
