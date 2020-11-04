from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.src.models.BaseModel import BaseModel

base = BaseModel()
Base = base.getDeclarative()


class TrainingUrlModel(Base):
    __tablename__ = "training_url"

    id = Column(
        Integer,
        primary_key=True,
        nullable=False
    )
    name = Column(
        String(1),
        nullable=False
    )

    url = Column(
        String(100),
        nullable=False
    )

    description = Column(
        String(1000),
        nullable=False
    )

    priority = Column(
        Integer,
        nullable=False
    )

    trainings = relationship("TrainingModel", back_populates="trainingUrl")
