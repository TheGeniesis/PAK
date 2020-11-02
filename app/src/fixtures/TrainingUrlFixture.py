from sqlalchemy.orm import sessionmaker

from app.src.models.BaseModel import BaseModel
from app.src.models.TrainingUrlModel import TrainingUrlModel


class TrainingUrlFixture:
    def generate(self):
        base = BaseModel()
        Session = sessionmaker(bind=base.getEngine())
        session = Session()

        ins = TrainingUrlModel(name="back exer", url="https://www.youtube.com/watch?v=Ddgmo7NFu1o", description="some descirption how to do exercise")
        session.add(ins)
        ins = TrainingUrlModel(name="other exerd", url="https://www.youtube.com/watch?v=5nZ8n1vUqVU", description="Some desc about exercise")
        session.add(ins)
        session.commit()