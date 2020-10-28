from app.src.queries.TrainingQuery import TrainingQuery


class MainViewHome:
    def configViewMain(self, view):
        view.main_text.setText("aVe Joseph")

        trainingQuery = TrainingQuery()

        view.training_today.setText(str(trainingQuery.findTodayTrainingQuantity()))
        view.training_this_week.setText(str(trainingQuery.findWeekTrainingQuantity()))
        view.training_this_month.setText(str(trainingQuery.findMonthTrainingQuantity()))
