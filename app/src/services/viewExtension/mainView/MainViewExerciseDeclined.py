import datetime
import textwrap

from sqlalchemy.orm import sessionmaker

from app.src.models.BaseModel import BaseModel
from app.src.models.TrainingModel import TrainingModel
from app.src.models.TrainingUrlModel import TrainingUrlModel
from app.src.services.core.dispatcher.EventDispatcher import EventDispatcher
from app.src.views.MainView import Ui_MainWindow


class MainViewExerciseDeclined:
    def configViewExerciseDeclined(self, view: Ui_MainWindow):
        view.b_exercise_declined_confirm.clicked.connect(lambda elem: self.commentAndRedirect(view))

    def commentAndRedirect(self, view: Ui_MainWindow):
        now = datetime.date.today()

        base = BaseModel()
        Session = sessionmaker(bind=base.getEngine())
        session = Session()

        trainingUrl = session.query(TrainingUrlModel).filter(TrainingUrlModel.id == int(view.video_id.text())).first()

        comment = textwrap.shorten(view.f_exercise_declined_comment.toPlainText(), 100)

        ins = TrainingModel(comment=comment, date=now, createdAt=now, updatedAt=now, trainingUrl=trainingUrl)
        session.add(ins)
        session.commit()

        EventDispatcher().getDispatcher().raise_event("onHomeViewReload", view=view)

        view.page_main.setCurrentWidget(view.view_main)
