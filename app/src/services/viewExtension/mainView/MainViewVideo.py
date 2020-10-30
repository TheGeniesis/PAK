from PyQt5.QtMultimediaWidgets import QVideoWidget


class MainViewVideo:
    def configViewVideo(self, view):
        view.video_box = QVideoWidget

        view.b_play_video.setEnabled(True)
        view.b_play_video.clicked.connect(self.loadHtml)

    def loadHtml(self):
        import webview
        import time
        print("adasdad")
        window = webview.create_window('Load HTML Example', html="""
        <html>
          <body>
             <iframe width="420" height="315"
            src="https://www.youtube.com/embed/tgbNymZ7vqY?autoplay=1&mute=1">
            </iframe> 
          </body>
        </html>
                """, fullscreen=True)
        webview.start(print, window)
