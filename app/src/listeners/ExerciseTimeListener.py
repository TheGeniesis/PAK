from plyer.utils import platform
from plyer import notification
from app.src.services.core.scheduler.BasicScheduler import BasicScheduler


class ExerciseTimeListener:
    def onKernelStart(self):
        scheduler = BasicScheduler()
        # @todo take it from db
        time = 30

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

