from plyer.utils import platform
from plyer import notification
from app.src.services.core.scheduler.BasicScheduler import BasicScheduler


class ExerciseTimeListener:
    def onKernelStart(self):
        scheduler = BasicScheduler()
        scheduler = scheduler.getScheduler()
        # @todo take it from db
        time = 30

        # Inform one minute before
        self.rescheduleJob(scheduler, time - 1, "exercise_block_scn_0")
        # inform a while before
        self.rescheduleJob(scheduler, time - 0.05, "exercise_block_scn_1")
        # @todo block screen
        self.rescheduleJob(scheduler, time, "exercise_block_scn_2")

    def notify(self):
        notification.notify(
            title='Exercise time is comming',
            message='Here is the message',
            app_name='Click-a-boo',
            app_icon='path/to/the/icon.' + ('ico' if platform == 'win' else 'png')
        )

    def rescheduleJob(self, scheduler, time: float, id: str):
        job = scheduler.get_job(id)
        if job:
            job.remove()

        scheduler.add_job(self.notify, 'interval', minutes=time, id=id)
