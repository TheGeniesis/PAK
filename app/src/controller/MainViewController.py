from app.src.controller.AbstractController import AbstractController
from app.src.services.core.dispatcher.EventDispatcher import EventDispatcher
from app.src.services.viewExtension.mainView.MainViewHome import MainViewHome
from app.src.services.viewExtension.mainView.MainViewSettings import MainViewSettings
from app.src.services.viewExtension.mainView.MainViewVideo import MainViewVideo
from app.src.services.viewExtension.mainView.MainViewSummary import MainViewSummary
from app.src.services.viewExtension.mainView.MainViewExerciseDeclined import MainViewExerciseDeclined
from app.src.services.viewExtension.mainView.MainViewExerciseGrade import MainViewExerciseGrade


class MainViewController(AbstractController):
    def index(self):
        file_name = "MainView"

        view = self.prepareView(file_name)

        # navigation
        view.nav_main.clicked.connect(lambda: view.page_main.setCurrentWidget(view.view_main))
        view.nav_settings.clicked.connect(lambda: view.page_main.setCurrentWidget(view.view_settings))
        view.nav_video.clicked.connect(lambda: view.page_main.setCurrentWidget(view.view_video))
        view.nav_summary.clicked.connect(lambda: view.page_main.setCurrentWidget(view.view_summary))

        # create view
        main_view_home = MainViewHome()
        main_view_home.configViewMain(view)

        main_view_settings = MainViewSettings()
        main_view_settings.configViewSettings(view)

        main_view_video = MainViewVideo()
        main_view_video.configViewVideo(view)

        main_view_summary = MainViewSummary()
        main_view_summary.configViewSummary(view)

        main_view_exercise_grade = MainViewExerciseGrade()
        main_view_exercise_grade.configViewExerciseGrade(view)

        main_view_exercise_declined = MainViewExerciseDeclined()
        main_view_exercise_declined.configViewExerciseDeclined(view)

        EventDispatcher().getDispatcher().raise_event("onNotify")

        return self.render()
