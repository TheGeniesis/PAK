from sqlalchemy import Column, Integer, Boolean
from app.src.models.BaseModel import BaseModel

base = BaseModel()
Base = base.getDeclarative()


class SettingModel(Base):
    __tablename__ = "setting"

    id = Column(
        Integer,
        primary_key=True,
        nullable=False
    )
    startWithSystem = Column(
        Boolean(),
        nullable=False
    )

    checkAbsence = Column(
        Boolean(),
        nullable=False
    )

    exerciseInterval = Column(
        Integer,
        nullable=False
    )
