from sqlalchemy.orm import sessionmaker

from app.src.models.TrainingModel import TrainingModel
from app.src.models.TrainingUrlModel import TrainingUrlModel
from app.src.services.core.dispatcher.EventDispatcher import EventDispatcher
from app.src.views.MainView import Ui_MainWindow
from app.src.models.BaseModel import BaseModel
import datetime


class MainViewExerciseGrade:
    def configViewExerciseGrade(self, view: Ui_MainWindow):
        view.b_exercise_grade_1.clicked.connect(lambda elem: self.gradeAndRedirect(view, 1))
        view.b_exercise_grade_2.clicked.connect(lambda elem: self.gradeAndRedirect(view, 2))
        view.b_exercise_grade_3.clicked.connect(lambda elem: self.gradeAndRedirect(view, 3))
        view.b_exercise_grade_4.clicked.connect(lambda elem: self.gradeAndRedirect(view, 4))
        view.b_exercise_grade_5.clicked.connect(lambda elem: self.gradeAndRedirect(view, 5))

    def gradeAndRedirect(self, view: Ui_MainWindow, grade: int):
        now = datetime.date.today()

        base = BaseModel()
        Session = sessionmaker(bind=base.getEngine())
        session = Session()

        trainingUrl = session.query(TrainingUrlModel).filter(TrainingUrlModel.id == int(view.video_id.text())).first()

        ins = TrainingModel(grade=grade, date=now, createdAt=now, updatedAt=now, trainingUrl=trainingUrl)
        session.add(ins)
        session.commit()

        EventDispatcher().getDispatcher().raise_event("onHomeViewReload", view=view)

        view.page_main.setCurrentWidget(view.view_main)
