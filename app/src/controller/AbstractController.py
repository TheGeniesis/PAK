from abc import ABCMeta
from PyQt5 import QtWidgets
import sys
from app.src.services.core.loader.ModuleLoader import ModuleLoader


class AbstractController(metaclass=ABCMeta):
    def __init__(self):
        self.__current_view = None
        self.__app = None

    def getCurrentView(self):
        return self.__current_view

    def prepareView(self, file_name: str):
        loader = ModuleLoader()
        view = loader.load(file_name, "app.src.views")

        if isinstance(self.__current_view, QtWidgets.QMainWindow):
            self.__current_view.hide()

        self.__app = QtWidgets.QApplication(sys.argv)
        self.__current_view = QtWidgets.QMainWindow()

        ui = view()
        ui.setupUi(self.__current_view)

        return ui

    def render(self):
        self.__current_view.show()
        sys.exit(self.__app.exec_())
