from app.src.controller.AbstractController import AbstractController
from app.src.services.viewExtension.mainView.MainViewHome import MainViewHome
from app.src.services.viewExtension.mainView.MainViewSettings import MainViewSettings


class MainViewController(AbstractController):
    def index(self):
        file_name = "MainView"

        view = self.prepareView(file_name)

        # navigation
        view.nav_main.clicked.connect(lambda: view.page_main.setCurrentWidget(view.view_main))
        view.nav_settings.clicked.connect(lambda: view.page_main.setCurrentWidget(view.view_settings))

        # Create view for main
        main_view_home = MainViewHome()
        main_view_home.configViewMain(view)

        # Create view for settings
        main_view_settings = MainViewSettings()
        main_view_settings.configViewSettings(view)

        return self.render()
