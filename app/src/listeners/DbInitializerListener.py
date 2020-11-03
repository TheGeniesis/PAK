from app.src.services.core.loader.FixtureLoader import FixtureLoader

# have to be here even it's not used
from app.src.models.TrainingUrlModel import TrainingUrlModel
from app.src.models.SettingModel import SettingModel


class DbInitializerListener:

    def eventList(self):
        return {
            "onKernelStart": {
                "action": self.onKernelStart,
                "priority": -200
            }
        }

    def onKernelStart(self):
        from app.src.models.BaseModel import BaseModel

        baseModel = BaseModel()
        declarative = baseModel.getDeclarative()
        declarative.metadata.create_all(baseModel.getEngine())

        fixture_loader = FixtureLoader()
        fixture_loader.load()
