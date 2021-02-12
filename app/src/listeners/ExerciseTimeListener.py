import os

from plyer.utils import platform
from plyer import notification
from sqlalchemy.orm import sessionmaker

from app.src.models.BaseModel import BaseModel
from app.src.models.SettingModel import SettingModel
from app.src.services.core.config.Config import Config
from app.src.services.core.scheduler.BasicScheduler import BasicScheduler

viewDict = {}


def getView(view_name):
    return viewDict.get(view_name)


class ExerciseTimeListener:
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
            # dodany nowy event, natomiast nie jesteśmy pewni gdzie jeszcze
            # należy go dodać
            "onTimerReset": {
                "action": self.setupNotifications,
                "priority": 0
            },
        }

    def setupNotifications(self):
        scheduler = BasicScheduler()
        base = BaseModel()
        Session = sessionmaker(bind=base.getEngine())
        session = Session()

        setting = session.query(SettingModel).first()

        time = setting.exerciseInterval
        if time > 2:
            # Inform one minute before
            scheduler.rescheduleJob(time - 1, "exercise_block_scn_0", self.notify)

        # inform a while before
        scheduler.rescheduleJob(time - 0.05, "exercise_block_scn_1", self.notify)
        # @todo block screen
        scheduler.rescheduleJob(time, "exercise_block_scn_2", self.notify)

        scheduler.getScheduler().add_job(self.changeView, 'interval', minutes=time, id="exercise_block_scn_3",
                                         replace_existing=True, )

    def notify(self):
        notification.notify(
            title='Exercise time is coming',
            message='Prepare for that!',
            app_name='Click-a-boo',
            app_icon=os.path.join(Config().getConfig()["path"],'app','src','views','test.') + ('ico' if platform == 'win' else 'png')

        )

    def changeView(self):
        view = getView("ui")
        view.page_main.setCurrentWidget(view.view_video)
