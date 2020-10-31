from PyQt5.QtMultimediaWidgets import QVideoWidget


class MainViewVideo:
    def configViewVideo(self, view):
        view.video_box = QVideoWidget

        view.b_video_play.setEnabled(True)
        view.b_video_play.clicked.connect(self.loadHtml)

        view.b_video_exercise_yes.clicked.connect(lambda: view.page_main.setCurrentWidget(view.view_exercise_grade))
        view.b_video_exercise_no.clicked.connect(lambda: view.page_main.setCurrentWidget(view.view_exercise_declined))

    def loadHtml(self):
        import webview
        window = webview.create_window('Load HTML Example', html="""
        <html>
          <body>
             <iframe width="420" height="315"
            src="https://www.youtube.com/watch?v=-Sh_fggFNFA&autoplay=1&mute=1">
            </iframe> 
          </body>
        </html>
                """, fullscreen=True)
        webview.start(print, window)
