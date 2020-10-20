from app.src.controller.AbstractController import AbstractController


class MainViewController(AbstractController):
    def index(self):
        file_name = "MainView"

        view = self.prepareView(file_name)
        view.main_text.setText("aVe Joseph")

        return self.render()
