from sqlalchemy.orm import sessionmaker

from app.src.models.BaseModel import BaseModel
from app.src.models.TrainingUrlModel import TrainingUrlModel
from app.src.services.core.config.Config import Config
from app.src.services.core.loader.ModuleLoader import ModuleLoader
import os
from glob import glob


class FixtureLoader:
    def load(self):
        base = BaseModel()
        Session = sessionmaker(bind=base.getEngine())
        session = Session()

        trainingUrl = session.query(TrainingUrlModel).first()
        if trainingUrl is None:

            # get all paths we use join to fix problem with "/" per os
            path = os.path.join(Config().getConfig()["path"], "app", "src", "fixtures")
            module_loader = ModuleLoader()
            for file in glob(os.path.join(path, "*.py")):
                module = module_loader.loadFromDir(file, "app.src.fixtures")

                module().generate()
