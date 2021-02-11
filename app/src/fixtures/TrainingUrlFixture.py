from sqlalchemy.orm import sessionmaker

from app.src.models.BaseModel import BaseModel
from app.src.models.TrainingUrlModel import TrainingUrlModel
from app.src.services.core.config.Config import Config


class TrainingUrlFixture:
    def generate(self):
        base = BaseModel()
        Session = sessionmaker(bind=base.getEngine())
        session = Session()
        config = Config().getConfig()

        ins = TrainingUrlModel(name="back exer", url="%s/video/small.mp4" % config["path"],
                               description="some descirption how to do exercise", priority=1)
        session.add(ins)
        ins = TrainingUrlModel(name="other exerd", url="%s/video/small2.mp4" % config["path"],
                               description="Some desc about exercise", priority=2)
        session.add(ins)
        session.commit()
