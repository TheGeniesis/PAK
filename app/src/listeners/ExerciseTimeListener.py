from plyer.utils import platform
from plyer import notification
from sqlalchemy.orm import sessionmaker

from app.src.models.BaseModel import BaseModel
from app.src.models.SettingModel import SettingModel
from app.src.services.core.scheduler.BasicScheduler import BasicScheduler
from app.src.views.MainView import Ui_MainWindow


class ExerciseTimeListener:
    __view: Ui_MainWindow
    def eventList(self):
        return {
            "onNotify": {
                "action": self.setupNotifications,
                "priority": 0
            },
            "onSettingsUpdate": {
                "action": self.setupNotifications,
                "priority": 0
            },
        }

    def setupNotifications(self, view: Ui_MainWindow):
        scheduler = BasicScheduler()
        base = BaseModel()
        Session = sessionmaker(bind=base.getEngine())
        session = Session()

        setting = session.query(SettingModel).first()

        time = setting.exerciseInterval
        time = 0.1
        if time > 2:
            # Inform one minute before
            scheduler.rescheduleJob(time - 1, "exercise_block_scn_0", self.notify)

        # inform a while before
        scheduler.rescheduleJob(time - 0.05, "exercise_block_scn_1", self.notify)
        # @todo block screen
        scheduler.rescheduleJob(time, "exercise_block_scn_2", self.notify)

        __view = view
        scheduler.getScheduler().add_job(self.changeView, 'interval', [view], minutes=time, id="exercise_block_scn_3", replace_existing=True, )

    def notify(self):
        notification.notify(
            title='Exercise time is coming',
            message='Here is the message',
            app_name='Click-a-boo',
            app_icon='path/to/the/icon.' + ('ico' if platform == 'win' else 'png')
        )

    def changeView(self, view):
        view.page_main.setCurrentWidget(view.view_video)
