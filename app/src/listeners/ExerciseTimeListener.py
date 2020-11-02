from plyer.utils import platform
from plyer import notification
from sqlalchemy.orm import sessionmaker

from app.src.models.BaseModel import BaseModel
from app.src.models.SettingModel import SettingModel
from app.src.services.core.scheduler.BasicScheduler import BasicScheduler


class ExerciseTimeListener:
    def onKernelStart(self):
        scheduler = BasicScheduler()

        base = BaseModel()
        Session = sessionmaker(bind=base.getEngine())
        session = Session()

        setting = session.query(SettingModel).first()

        time = setting.exerciseInterval

        # Inform one minute before
        scheduler.rescheduleJob(time - 1, "exercise_block_scn_0", self.notify)
        # inform a while before
        scheduler.rescheduleJob(time - 0.05, "exercise_block_scn_1", self.notify)
        # @todo block screen
        scheduler.rescheduleJob(time, "exercise_block_scn_2", self.notify)

    def notify(self):
        notification.notify(
            title='Exercise time is coming',
            message='Here is the message',
            app_name='Click-a-boo',
            app_icon='path/to/the/icon.' + ('ico' if platform == 'win' else 'png')
        )

