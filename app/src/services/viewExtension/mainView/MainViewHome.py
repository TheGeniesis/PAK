class MainViewHome:
    def configViewMain(self, view):
        view.main_text.setText("aVe Joseph")
        from sqlalchemy.sql import select
        from sqlalchemy import create_engine
        engine = create_engine('sqlite:///click-a-boo.db', echo=True)

        from app.src.models.TrainingModel import TrainingModel

        # training = TrainingModel()

        # s = select([training])
        # conn = engine.connect()
        # result = conn.execute(s)
        # print (result)
        # view.training_today.setText()
