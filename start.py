from app.src.controller.MainViewController import MainViewController

from app.src.services.core.config.Config import Config

import os

from app.src.services.core.dispatcher.EventDispatcher import EventDispatcher
from app.src.services.core.loader.ListenerLoader import ListenerLoader

config = Config()
config.init({
    "path": os.getcwd()
})

ListenerLoader().load()
EventDispatcher().getDispatcher().raise_event("onKernelStart")

ctl = MainViewController()
ctl.index()
