from plyer.utils import platform
from plyer import notification
from sqlalchemy.orm import sessionmaker

from app.src.models.BaseModel import BaseModel
from app.src.models.SettingModel import SettingModel
from app.src.services.core.scheduler.BasicScheduler import BasicScheduler
from app.src.services.detection.FaceDetector import FaceDetector
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
            },

            "onKernelStart": {
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
            # tutaj nie jestem pewien czy nie powinno się dodawać
            # rescheduleJob().add_job bo w zasadzie add_job
            # realizuje się wewnątrz tej funkcji
        else:
            scheduler.getScheduler().get_job("absence_timer").remove()

    def runAbsenceTimer(self, setting=SettingModel):

        base = BaseModel()
        Session = sessionmaker(bind=base.getEngine())
        session = Session()

        face_detector = FaceDetector()
        if not face_detector.isUserDetected():
            setting.timeAbsence += 1
        else:
            setting.timeAbsence = 0

        if setting.timeAbsence == 3:
            # odpalenie drugiego listenera, który wszystko resetuje i kod biegnie od nowa
            EventDispatcher().getDispatcher().raise_event("onSettingsUpdate")
            setting.timeAbsence = 0

        session.merge(setting)
        session.commit()