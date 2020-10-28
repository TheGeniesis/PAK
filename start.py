from app.src.controller.MainViewController import MainViewController

from app.src.listeners.ExerciseTimeListener import ExerciseTimeListener
from app.src.services.core.config.Config import Config

# have to be here even it's not used
from app.src.models import TrainingModel, TrainingUrlModel

import os

config = Config()
config.init({
    "path": os.getcwd()
})

# @todo run db creation in listener
def initDb():
    from app.src.models.BaseModel import BaseModel

    baseModel = BaseModel()
    declarative = baseModel.getDeclarative()
    declarative.metadata.create_all(baseModel.getEngine())


initDb()

# @todo use normal event system
a = ExerciseTimeListener()
a.onKernelStart()

ctl = MainViewController()
ctl.index()
