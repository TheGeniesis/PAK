from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class TrainingModel(Base):
    __tablename__ = "training"

    id = Column(
        Integer(),
        primary_key=True,
        nullable=False
    )
    grade = Column(
        Integer(),
        nullable=True
    )

    comment = Column(
        String(100),
        nullable=True
    )

    trainingUrlId = Column(Integer(), ForeignKey('training_url.id'))
    trainingUrl = relationship("app.src.models.TrainingUrlModel", back_populates="trainings")

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

