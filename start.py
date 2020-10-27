from app.src.controller.MainViewController import MainViewController

from app.src.listeners.ExerciseTimeListener import ExerciseTimeListener
from app.src.services.core.config.Config import Config
import os

config = Config()
config.init({
    "path": os.getcwd()
})


def execute():
    from sqlalchemy import create_engine, MetaData
    from app.src.services.core.config.Config import Config


    config = Config()
    config = config.getConfig()
    engine = create_engine(config["DATABASE"]["PATH"], echo=True)

    meta = MetaData()
    meta.tables.values()

    from app.src.models import TrainingModel, TrainingUrlModel

    meta.create_all(engine)


execute()

# @todo use normal event system
a = ExerciseTimeListener()
a.onKernelStart()

ctl = MainViewController()
ctl.index()
