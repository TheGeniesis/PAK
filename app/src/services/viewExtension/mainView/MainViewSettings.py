from sqlalchemy.orm import sessionmaker

from app.src.models.BaseModel import BaseModel
from app.src.models.SettingModel import SettingModel
from app.src.views.MainView import Ui_MainWindow

class MainViewSettings:
    def configViewSettings(self, view: Ui_MainWindow):

        base = BaseModel()
        Session = sessionmaker(bind=base.getEngine())
        session = Session()

        setting: SettingModel = session.query(SettingModel).first()

        view.f_settings_start_with_os.setChecked(setting.startWithSystem)

        view.f_settings_check_absence.setChecked(setting.checkAbsence)

        view.f_settings_exercise_interval.setMinimum(1)
        view.f_settings_exercise_interval.setMaximum(90)
        view.f_settings_exercise_interval.setValue(setting.exerciseInterval / 60)

        view.b_settings_confirm.clicked.connect(lambda elem: self.save(view, setting))

    def save(self, view: Ui_MainWindow, setting: SettingModel):

        setting.checkAbsence = view.f_settings_check_absence.isChecked()
        setting.startWithSystem = view.f_settings_start_with_os.isChecked()
        setting.exerciseInterval = view.f_settings_exercise_interval.value() * 60

        base = BaseModel()
        Session = sessionmaker(bind=base.getEngine())
        session = Session()

        session.merge(setting)
        session.commit()
