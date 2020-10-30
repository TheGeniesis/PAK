from app.src.controller.AbstractController import AbstractController
from app.src.services.viewExtension.mainView.MainViewHome import MainViewHome
from app.src.services.viewExtension.mainView.MainViewSettings import MainViewSettings
from app.src.services.viewExtension.mainView.MainViewVideo import MainViewVideo
from app.src.services.viewExtension.mainView.MainViewSummary import MainViewSummary


class MainViewController(AbstractController):
    def index(self):
        file_name = "MainView"

        view = self.prepareView(file_name)

        # navigation
        view.nav_main.clicked.connect(lambda: view.page_main.setCurrentWidget(view.view_main))
        view.nav_settings.clicked.connect(lambda: view.page_main.setCurrentWidget(view.view_settings))
        view.nav_video.clicked.connect(lambda: view.page_main.setCurrentWidget(view.view_video))
        view.nav_summary.clicked.connect(lambda: view.page_main.setCurrentWidget(view.view_summary))

        # Create view for main
        main_view_home = MainViewHome()
        main_view_home.configViewMain(view)

        # Create view for settings
        main_view_settings = MainViewSettings()
        main_view_settings.configViewSettings(view)

        # Create view for video
        main_view_settings = MainViewVideo()
        main_view_settings.configViewVideo(view)

        # Create view for summary
        main_view_settings = MainViewSummary()
        main_view_settings.configViewSummary(view)

        return self.render()
