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
        MainWindow.resize(1106, 769)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.page_main = QtWidgets.QStackedWidget(self.centralwidget)
        self.page_main.setGeometry(QtCore.QRect(200, 20, 741, 731))
        self.page_main.setObjectName("page_main")
        self.view_main = QtWidgets.QWidget()
        self.view_main.setObjectName("view_main")
        self.main_training_today = QtWidgets.QLabel(self.view_main)
        self.main_training_today.setGeometry(QtCore.QRect(80, 340, 67, 17))
        self.main_training_today.setObjectName("main_training_today")
        self.label_3 = QtWidgets.QLabel(self.view_main)
        self.label_3.setGeometry(QtCore.QRect(360, 290, 161, 17))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.view_main)
        self.label_2.setGeometry(QtCore.QRect(190, 290, 141, 17))
        self.label_2.setObjectName("label_2")
        self.main_training_this_week = QtWidgets.QLabel(self.view_main)
        self.main_training_this_week.setGeometry(QtCore.QRect(210, 330, 67, 17))
        self.main_training_this_week.setObjectName("main_training_this_week")
        self.main_training_this_month = QtWidgets.QLabel(self.view_main)
        self.main_training_this_month.setGeometry(QtCore.QRect(380, 340, 67, 17))
        self.main_training_this_month.setObjectName("main_training_this_month")
        self.main_text = QtWidgets.QLabel(self.view_main)
        self.main_text.setGeometry(QtCore.QRect(260, 50, 67, 17))
        self.main_text.setObjectName("main_text")
        self.label = QtWidgets.QLabel(self.view_main)
        self.label.setGeometry(QtCore.QRect(60, 290, 141, 17))
        self.label.setObjectName("label")
        self.page_main.addWidget(self.view_main)
        self.view_video = QtWidgets.QWidget()
        self.view_video.setObjectName("view_video")
        self.label_5 = QtWidgets.QLabel(self.view_video)
        self.label_5.setGeometry(QtCore.QRect(170, 500, 281, 61))
        self.label_5.setObjectName("label_5")
        self.b_video_exercise_yes = QtWidgets.QPushButton(self.view_video)
        self.b_video_exercise_yes.setGeometry(QtCore.QRect(170, 590, 89, 25))
        self.b_video_exercise_yes.setObjectName("b_video_exercise_yes")
        self.b_video_exercise_no = QtWidgets.QPushButton(self.view_video)
        self.b_video_exercise_no.setGeometry(QtCore.QRect(340, 590, 89, 25))
        self.b_video_exercise_no.setObjectName("b_video_exercise_no")
        self.video_widget = QtWidgets.QWidget(self.view_video)
        self.video_widget.setGeometry(QtCore.QRect(90, 30, 541, 451))
        self.video_widget.setObjectName("video_widget")
        self.f_video_length = QtWidgets.QSlider(self.video_widget)
        self.f_video_length.setGeometry(QtCore.QRect(30, 320, 160, 16))
        self.f_video_length.setOrientation(QtCore.Qt.Horizontal)
        self.f_video_length.setObjectName("f_video_length")
        self.video_box = QtWidgets.QWidget(self.video_widget)
        self.video_box.setGeometry(QtCore.QRect(40, 30, 471, 221))
        self.video_box.setObjectName("video_box")
        self.video_id = QtWidgets.QLabel(self.video_box)
        self.video_id.setGeometry(QtCore.QRect(180, 40, 67, 17))
        self.video_id.setObjectName("video_id")
        self.b_video_play = QtWidgets.QPushButton(self.video_widget)
        self.b_video_play.setGeometry(QtCore.QRect(40, 270, 89, 25))
        self.b_video_play.setObjectName("b_video_play")
        self.video_media_player = QtWidgets.QWidget(self.video_widget)
        self.video_media_player.setGeometry(QtCore.QRect(20, 50, 120, 80))
        self.video_media_player.setObjectName("video_media_player")
        self.page_main.addWidget(self.view_video)
        self.view_exercise_declined = QtWidgets.QWidget()
        self.view_exercise_declined.setObjectName("view_exercise_declined")
        self.label_7 = QtWidgets.QLabel(self.view_exercise_declined)
        self.label_7.setGeometry(QtCore.QRect(220, 120, 461, 61))
        self.label_7.setObjectName("label_7")
        self.f_exercise_declined_comment = QtWidgets.QPlainTextEdit(self.view_exercise_declined)
        self.f_exercise_declined_comment.setGeometry(QtCore.QRect(140, 260, 391, 181))
        self.f_exercise_declined_comment.setObjectName("f_exercise_declined_comment")
        self.b_exercise_declined_confirm = QtWidgets.QPushButton(self.view_exercise_declined)
        self.b_exercise_declined_confirm.setGeometry(QtCore.QRect(470, 490, 89, 25))
        self.b_exercise_declined_confirm.setObjectName("b_exercise_declined_confirm")
        self.page_main.addWidget(self.view_exercise_declined)
        self.view_exercise_grade = QtWidgets.QWidget()
        self.view_exercise_grade.setObjectName("view_exercise_grade")
        self.b_exercise_grade_1 = QtWidgets.QPushButton(self.view_exercise_grade)
        self.b_exercise_grade_1.setGeometry(QtCore.QRect(90, 380, 89, 25))
        self.b_exercise_grade_1.setObjectName("b_exercise_grade_1")
        self.b_exercise_grade_2 = QtWidgets.QPushButton(self.view_exercise_grade)
        self.b_exercise_grade_2.setGeometry(QtCore.QRect(210, 390, 89, 25))
        self.b_exercise_grade_2.setObjectName("b_exercise_grade_2")
        self.b_exercise_grade_3 = QtWidgets.QPushButton(self.view_exercise_grade)
        self.b_exercise_grade_3.setGeometry(QtCore.QRect(310, 380, 89, 25))
        self.b_exercise_grade_3.setObjectName("b_exercise_grade_3")
        self.b_exercise_grade_4 = QtWidgets.QPushButton(self.view_exercise_grade)
        self.b_exercise_grade_4.setGeometry(QtCore.QRect(410, 390, 89, 25))
        self.b_exercise_grade_4.setObjectName("b_exercise_grade_4")
        self.b_exercise_grade_5 = QtWidgets.QPushButton(self.view_exercise_grade)
        self.b_exercise_grade_5.setGeometry(QtCore.QRect(530, 380, 89, 25))
        self.b_exercise_grade_5.setObjectName("b_exercise_grade_5")
        self.label_8 = QtWidgets.QLabel(self.view_exercise_grade)
        self.label_8.setGeometry(QtCore.QRect(180, 160, 371, 61))
        self.label_8.setObjectName("label_8")
        self.page_main.addWidget(self.view_exercise_grade)
        self.view_settings = QtWidgets.QWidget()
        self.view_settings.setObjectName("view_settings")
        self.label_4 = QtWidgets.QLabel(self.view_settings)
        self.label_4.setGeometry(QtCore.QRect(280, 70, 67, 17))
        self.label_4.setObjectName("label_4")
        self.label_9 = QtWidgets.QLabel(self.view_settings)
        self.label_9.setGeometry(QtCore.QRect(280, 130, 231, 21))
        self.label_9.setObjectName("label_9")
        self.f_settings_check_absence = QtWidgets.QCheckBox(self.view_settings)
        self.f_settings_check_absence.setGeometry(QtCore.QRect(300, 260, 241, 23))
        self.f_settings_check_absence.setObjectName("f_settings_check_absence")
        self.f_settings_start_with_os = QtWidgets.QCheckBox(self.view_settings)
        self.f_settings_start_with_os.setGeometry(QtCore.QRect(290, 350, 231, 23))
        self.f_settings_start_with_os.setObjectName("f_settings_start_with_os")
        self.b_settings_confirm = QtWidgets.QPushButton(self.view_settings)
        self.b_settings_confirm.setGeometry(QtCore.QRect(420, 430, 89, 25))
        self.b_settings_confirm.setObjectName("b_settings_confirm")
        self.f_settings_exercise_interval = QtWidgets.QSlider(self.view_settings)
        self.f_settings_exercise_interval.setGeometry(QtCore.QRect(320, 200, 160, 16))
        self.f_settings_exercise_interval.setOrientation(QtCore.Qt.Horizontal)
        self.f_settings_exercise_interval.setObjectName("f_settings_exercise_interval")
        self.page_main.addWidget(self.view_settings)
        self.view_summary = QtWidgets.QWidget()
        self.view_summary.setObjectName("view_summary")
        self.label_6 = QtWidgets.QLabel(self.view_summary)
        self.label_6.setGeometry(QtCore.QRect(330, 100, 67, 17))
        self.label_6.setObjectName("label_6")
        self.page_main.addWidget(self.view_summary)
        self.nav_main = QtWidgets.QPushButton(self.centralwidget)
        self.nav_main.setGeometry(QtCore.QRect(10, 10, 89, 25))
        self.nav_main.setObjectName("nav_main")
        self.nav_settings = QtWidgets.QPushButton(self.centralwidget)
        self.nav_settings.setGeometry(QtCore.QRect(0, 60, 89, 25))
        self.nav_settings.setObjectName("nav_settings")
        self.nav_video = QtWidgets.QPushButton(self.centralwidget)
        self.nav_video.setGeometry(QtCore.QRect(20, 100, 89, 25))
        self.nav_video.setObjectName("nav_video")
        self.nav_summary = QtWidgets.QPushButton(self.centralwidget)
        self.nav_summary.setGeometry(QtCore.QRect(20, 150, 89, 25))
        self.nav_summary.setObjectName("nav_summary")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1106, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.page_main.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main_training_today.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "trenings this month"))
        self.label_2.setText(_translate("MainWindow", "trenings this week"))
        self.main_training_this_week.setText(_translate("MainWindow", "TextLabel"))
        self.main_training_this_month.setText(_translate("MainWindow", "TextLabel"))
        self.main_text.setText(_translate("MainWindow", "Hellp"))
        self.label.setText(_translate("MainWindow", "trenings today"))
        self.label_5.setText(_translate("MainWindow", "Do you want to do exercies now"))
        self.b_video_exercise_yes.setText(_translate("MainWindow", "Yes"))
        self.b_video_exercise_no.setText(_translate("MainWindow", "No"))
        self.video_id.setText(_translate("MainWindow", "1"))
        self.b_video_play.setText(_translate("MainWindow", "Play"))
        self.label_7.setText(_translate("MainWindow", "Why did you decline exercieses?"))
        self.b_exercise_declined_confirm.setText(_translate("MainWindow", "Confirm"))
        self.b_exercise_grade_1.setText(_translate("MainWindow", "1"))
        self.b_exercise_grade_2.setText(_translate("MainWindow", "2"))
        self.b_exercise_grade_3.setText(_translate("MainWindow", "3"))
        self.b_exercise_grade_4.setText(_translate("MainWindow", "4"))
        self.b_exercise_grade_5.setText(_translate("MainWindow", "5"))
        self.label_8.setText(_translate("MainWindow", "Grade exercise"))
        self.label_4.setText(_translate("MainWindow", "Settings"))
        self.label_9.setText(_translate("MainWindow", "Exercise interval"))
        self.f_settings_check_absence.setText(_translate("MainWindow", "Check absence"))
        self.f_settings_start_with_os.setText(_translate("MainWindow", "Start with system"))
        self.b_settings_confirm.setText(_translate("MainWindow", "Confirm"))
        self.label_6.setText(_translate("MainWindow", "Summary"))
        self.nav_main.setText(_translate("MainWindow", "Homepage"))
        self.nav_settings.setText(_translate("MainWindow", "Settings"))
        self.nav_video.setText(_translate("MainWindow", "Video"))
        self.nav_summary.setText(_translate("MainWindow", "Summary"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
