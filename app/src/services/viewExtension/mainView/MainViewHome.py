from app.src.queries.TrainingQuery import TrainingQuery


class MainViewHome:
    def configViewMain(self, view):
        view.main_text.setText("aVe Joseph")

        trainingQuery = TrainingQuery()

        view.main_training_today.setText(str(trainingQuery.findTodayTrainingQuantity()))
        view.main_training_this_week.setText(str(trainingQuery.findWeekTrainingQuantity()))
        view.main_training_this_month.setText(str(trainingQuery.findMonthTrainingQuantity()))
