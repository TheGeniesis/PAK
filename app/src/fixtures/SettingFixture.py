from sqlalchemy.orm import sessionmaker

from app.src.models.BaseModel import BaseModel
from app.src.models.SettingModel import SettingModel


class SettingFixture:
    def generate(self):
        base = BaseModel()
        Session = sessionmaker(bind=base.getEngine())
        session = Session()

        ins = SettingModel(startWithSystem=False, checkAbsence=True, exerciseInterval=30)
        session.add(ins)
        session.commit()
