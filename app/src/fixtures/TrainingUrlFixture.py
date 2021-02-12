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

        ins = TrainingUrlModel(name="Triceps", url=os.path.join(Config().getConfig()["path"], 'video', 'Triceps.wmv'),
                               description="Triceps exercise", priority=1)
        session.add(ins)
        ins = TrainingUrlModel(name="Biceps", url=os.path.join(Config().getConfig()["path"], 'video', 'Biceps.mp4'),
                               description="Bending for overall back relaxation", priority=2)
        session.add(ins)
        ins = TrainingUrlModel(name="Side Bends", url=os.path.join(Config().getConfig()["path"], 'video'
                                                                   ,'Side bends.mp4'),
                               description="Sideways bending to train lats and obliques", priority=3)
        session.add(ins)
        ins = TrainingUrlModel(name="Biceps Stretch", url=os.path.join(Config().getConfig()["path"], 'video',
                                                                       'Spotmarch.mp4'),
                               description="Spot marching exercise", priority=4)
        session.add(ins)
        ins = TrainingUrlModel(name="Forearm Stretch", url=os.path.join(Config().getConfig()["path"], 'video',
                                                                        'Forearm stretch.mp4'),
                               description="Palm facing up / Palm facing down for forearm flexors exercise", priority=5)
        session.add(ins)
        ins = TrainingUrlModel(name="Hyperextension", url=os.path.join(Config().getConfig()["path"], 'video',
                                                                       'Hyperextension.mp4'),
                               description="Back extension and abs stretch exercise", priority=6)
        session.add(ins)
        ins = TrainingUrlModel(name="Neck Stretch", url=os.path.join(Config().getConfig()["path"], 'video',
                                                                     'Neck stretch.mp4'),
                               description="Front, back and side of the neck exercise", priority=7)
        session.add(ins)
        ins = TrainingUrlModel(name="Palming", url=os.path.join(Config().getConfig()["path"], 'video','Palming.mp4'),
                               description="Eye and facial muscles relaxation exercise", priority=8)
        session.add(ins)
        ins = TrainingUrlModel(name="Shrugs", url=os.path.join(Config().getConfig()["path"], 'video','Shrugs.mp4'),
                               description="Trapezius and neck muscles exercise", priority=9)
        session.add(ins)
        ins = TrainingUrlModel(name="Full Body Stretch", url=os.path.join(Config().getConfig()["path"], 'video',
                                                                          'Full body stretch.mp4'),
                               description="Overall body exercise", priority=10)
        session.add(ins)
        ins = TrainingUrlModel(name="Torso Twist", url=os.path.join(Config().getConfig()["path"], 'video',
                                                                    'Torso twist.mp4'),
                               description="Spinal mobility exercise", priority=11)
        session.add(ins)
        ins = TrainingUrlModel(name="Forward bending", url=os.path.join(Config().getConfig()["path"], 'video',
                                                                        'Forward bending.mp4'),
                               description="Forward bending exercise", priority=12)
        session.add(ins)
        session.commit()
