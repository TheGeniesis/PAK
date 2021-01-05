from app.src.queries.TrainingQuery import TrainingQuery
from app.src.views.MainView import Ui_MainWindow


class MainViewSummary:
    def configViewSummary(self, view: Ui_MainWindow):
        view.summary_calendar.clicked.connect(lambda elem: self.showDetails(view, elem))

    def showDetails(self, view: Ui_MainWindow, elem):
        trainingQuery = TrainingQuery()

        view.summary_exercises_amount.setText(str(trainingQuery.findTrainingQuantityForDay(elem.toPyDate())))
