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
            path = Config().getConfig()["path"] + os.path.join("app", "src", "fixtures")
            module_loader = ModuleLoader()

            for file in glob(os.path.join(path, "*.py")):
                # we have filename = /path/filename.py, we
                # first we remove path
                # os.sep returns correct "/" per os
                class_name = file.rsplit(os.sep, 1)[-1]
                # we have class_name = filename.py
                # and now we remove extension
                class_name = class_name[:-3]
                # we have class_name = filename

                module = module_loader.load(class_name, "app.src.fixtures")
                module.generate()
