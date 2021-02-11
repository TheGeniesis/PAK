import os

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

        ins = TrainingUrlModel(name="Spot March", url=os.path.join(Config().getConfig()["path"], 'video','Triceps.wmv'),
                               description="Marching in place exercise", priority=1)
        session.add(ins)
        ins = TrainingUrlModel(name="Forward Bending", url="%s/video/bending.mp4" % config["path"],
                               description="Bending for overall back relaxation", priority=2)
        session.add(ins)
        ins = TrainingUrlModel(name="Side Bends", url="%s/video/bends.mp4" % config["path"],
                               description="Sideways bending to train lats and obliques", priority=3)
        session.add(ins)
        ins = TrainingUrlModel(name="Biceps Stretch", url="%s/video/biceps.mp4" % config["path"],
                               description="Stretching for biceps exercise", priority=4)
        session.add(ins)
        ins = TrainingUrlModel(name="Forearm Stretch", url="%s/video/forearm.mp4" % config["path"],
                               description="Palm facing up / Palm facing down for forearm flexors exercise", priority=5)
        session.add(ins)
        ins = TrainingUrlModel(name="Hyperextension", url="%s/video/hyperextension.mp4" % config["path"],
                               description="Back extension and abs stretch exercise", priority=6)
        session.add(ins)
        ins = TrainingUrlModel(name="Neck Stretch", url="%s/video/neck.mp4" % config["path"],
                               description="Front, back and side of the neck exercise", priority=7)
        session.add(ins)
        ins = TrainingUrlModel(name="Palming", url="%s/video/palming.mp4" % config["path"],
                               description="Eye and facial muscles relaxation exercise", priority=8)
        session.add(ins)
        ins = TrainingUrlModel(name="Shrugs", url="%s/video/shrugs.mp4" % config["path"],
                               description="Trapezius and neck muscles exercise", priority=9)
        session.add(ins)
        ins = TrainingUrlModel(name="Full Body Stretch", url="%s/video/shrugs.mp4" % config["path"],
                               description="Overall body exercise", priority=10)
        session.add(ins)
        ins = TrainingUrlModel(name="Torso Twist", url="%s/video/torso.mp4" % config["path"],
                               description="Spinal mobility exercise", priority=11)
        session.add(ins)
        ins = TrainingUrlModel(name="Triceps Stretch", url="%s/video/triceps.mp4" % config["path"],
                               description="Triceps exercise", priority=12)
        session.add(ins)
        session.commit()
