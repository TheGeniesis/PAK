from sqlalchemy import func
from datetime import date
import datetime
from app.src.models.TrainingModel import TrainingModel
from sqlalchemy import and_
from sqlalchemy.orm import sessionmaker
from app.src.models.BaseModel import BaseModel


class TrainingQuery:

    def findTodayTrainingQuantity(self):
        base = BaseModel()

        Session = sessionmaker(bind=base.getEngine())
        session = Session()

        today = date.today()
        startDay = today.strftime("%Y-%m-%d 00:00:00")

        tomorrow = today + datetime.timedelta(days=1)
        endDay = tomorrow.strftime("%Y-%m-%d 00:00:00")
        query = session.query("app.src.models.TrainingModel")
        query = query.filter(
            and_(
                TrainingModel.grade != None,
                TrainingModel.createdAt >= startDay,
                TrainingModel.createdAt < endDay,
            )
        )
        return query.with_entities(func.count()).scalar()

    def findWeekTrainingQuantity(self):
        base = BaseModel()

        Session = sessionmaker(bind=base.getEngine())
        session = Session()

        startDay = date.today() - datetime.timedelta(days=date.today().isoweekday() % 7)
        startDay = startDay.strftime("%Y-%m-%d 00:00:00")

        tomorrow = date.today() + datetime.timedelta(days=1)
        endDay = tomorrow.strftime("%Y-%m-%d 00:00:00")
        query = session.query("app.src.models.TrainingModel")
        query = query.filter(
            and_(
                TrainingModel.grade != None,
                TrainingModel.createdAt >= startDay,
                TrainingModel.createdAt < endDay,
            )
        )
        return query.with_entities(func.count()).scalar()

    def findMonthTrainingQuantity(self):
        base = BaseModel()

        Session = sessionmaker(bind=base.getEngine())
        session = Session()

        startDay = date.today().replace(day=1)
        startDay = startDay.strftime("%Y-%m-%d 00:00:00")

        tomorrow = date.today() + datetime.timedelta(days=1)
        endDay = tomorrow.strftime("%Y-%m-%d 00:00:00")
        query = session.query("app.src.models.TrainingModel")
        query = query.filter(
            and_(
                TrainingModel.grade != None,
                TrainingModel.createdAt >= startDay,
                TrainingModel.createdAt < endDay,
            )
        )
        return query.with_entities(func.count()).scalar()
