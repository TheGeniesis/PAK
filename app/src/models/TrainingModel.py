from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.src.models.BaseModel import BaseModel

base = BaseModel()
Base = base.getDeclarative()


class TrainingModel(Base):
    __tablename__ = "training"

    id = Column(
        Integer(),
        primary_key=True,
        nullable=False
    )
    grade = Column(
        Integer(),
        nullable=True,
        default=None
    )

    comment = Column(
        String(100),
        nullable=True
    )

    trainingUrlId = Column(Integer(), ForeignKey('training_url.id'))
    trainingUrl = relationship("TrainingUrlModel", back_populates="trainings")

    date = Column(
        DateTime(),
        nullable=False
    )

    createdAt = Column(
        DateTime(),
        nullable=False
    )

    updatedAt = Column(
        DateTime(),
        nullable=False
    )
