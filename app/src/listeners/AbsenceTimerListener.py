from plyer.utils import platform
from plyer import notification
from sqlalchemy.orm import sessionmaker
from app.src.models.BaseModel import BaseModel
from app.src.models.SettingModel import SettingModel
from app.src.services.core.scheduler.BasicScheduler import BasicScheduler
from app.src.services.detection import FaceDetector
from app.src.views.MainView import Ui_MainWindow
from app.src.services.core.dispatcher.EventDispatcher import EventDispatcher

viewDict = {}


def getView(view_name):
    return viewDict.get(view_name)


class AbsenceTimerListener:
    def eventList(self):
        return {
            "onSettingsUpdate": {
                "action": self.setupCamera,
                "priority": 0
            }
        }

    def setupCamera(self):
        scheduler = BasicScheduler()
        base = BaseModel()
        Session = sessionmaker(bind=base.getEngine())
        session = Session()
        setting = session.query(SettingModel).first()
        time = 2

        if setting.checkAbsence:
            scheduler.rescheduleJob(time, "absence_timer",
                                    self.runAbsenceTimer)

        else:
            scheduler.getScheduler().remove_job(id="absence_timer")

    def runAbsenceTimer(self, setting=SettingModel):

        base = BaseModel()
        Session = sessionmaker(bind=base.getEngine())
        session = Session()

        if not FaceDetector.isUserDetected():
            setting.timeAbsence += 1
        else:
            setting.timeAbsence = 0

        if setting.timeAbsence == 3:
            # kod na reset głównego timera
            setting.timeAbsence = 0

        session.merge(setting)
        session.commit()