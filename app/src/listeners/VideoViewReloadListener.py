from app.src.services.viewExtension.mainView.MainViewVideo import MainViewVideo
from app.src.views.MainView import Ui_MainWindow


class VideoViewReloadListener:
    def eventList(self):
        return {
            "onVideoViewReload": {
                "action": self.reload,
                "priority": 0
            }
        }

    def reload(self, view: Ui_MainWindow):
        main_view_video = MainViewVideo()
        #quick fix for video (second video didin't run
        main_view_video.configViewVideo(view)
        main_view_video.configViewVideo(view)
