from PyQt5.QtMultimediaWidgets import QVideoWidget
from sqlalchemy.orm import sessionmaker
from PyQt5.QtCore import QUrl
from app.src.models.BaseModel import BaseModel
from app.src.models.TrainingUrlModel import TrainingUrlModel
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from app.src.views.MainView import Ui_MainWindow


class MainViewVideo:
    view: Ui_MainWindow

    def configViewVideo(self, view: Ui_MainWindow):
        self.view = view

        view.video_widget = QVideoWidget(view.video_box)
        view.video_box.show()
        view.video_widget.setFixedSize(view.video_box.size())

        base = BaseModel()
        Session = sessionmaker(bind=base.getEngine())
        session = Session()

        trainingUrl = session.query(TrainingUrlModel).order_by(TrainingUrlModel.priority).first()



        view.video_id = trainingUrl.id
        view.video_media_player = QMediaPlayer(None, QMediaPlayer.StreamPlayback)
        view.f_video_length.setRange(0, 0)
        view.f_video_length.sliderMoved.connect(self.setPosition)

        view.video_media_player.setMedia(
            QMediaContent(QUrl.fromLocalFile(trainingUrl.url)))

        view.video_media_player.setVideoOutput(view.video_widget)
        view.video_media_player.positionChanged.connect(self.positionChanged)
        view.video_media_player.durationChanged.connect(self.durationChanged)

        view.b_video_play.setEnabled(True)
        view.b_video_play.clicked.connect(lambda: self.play(view))

        view.b_video_exercise_yes.clicked.connect(lambda: view.page_main.setCurrentWidget(view.view_exercise_grade))
        view.b_video_exercise_no.clicked.connect(lambda: view.page_main.setCurrentWidget(view.view_exercise_declined))

    def play(self, view: Ui_MainWindow):
        if view.video_media_player.state() == QMediaPlayer.PlayingState:
            view.video_media_player.pause()
            return
        view.video_media_player.play()



    def positionChanged(self, position):
        self.view.f_video_length.setValue(position)

    def durationChanged(self, duration):
        self.view.f_video_length.setRange(0, duration)

    def setPosition(self, position):
        self.view.video_media_player.setPosition(position)
