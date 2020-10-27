from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


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

    trainings = relationship("app.src.models.TrainingModel", back_populates="trainingUrl")

