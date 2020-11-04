from app.src.services.viewExtension.mainView.MainViewHome import MainViewHome
from app.src.views.MainView import Ui_MainWindow


class HomeViewReloadListener:
    def eventList(self):
        return {
            "onHomeViewReload": {
                "action": self.reload,
                "priority": 0
            }
        }

    def reload(self, view: Ui_MainWindow):
        main_view_home = MainViewHome()
        main_view_home.configViewMain(view)
