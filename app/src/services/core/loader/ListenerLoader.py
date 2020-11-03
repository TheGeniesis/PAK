from EventNotifier import Notifier

from app.src.services.core.config.Config import Config
from app.src.services.core.dispatcher.EventDispatcher import EventDispatcher
from app.src.services.core.loader.ModuleLoader import ModuleLoader
import os
from glob import glob


class ListenerLoader:
    def load(self):
        # get all paths we use join to fix problem with "/" per os
        path = os.path.join(Config().getConfig()["path"], "app", "src", "listeners")
        module_loader = ModuleLoader()

        event_list = list()
        for file in glob(os.path.join(path, "*.py")):
            module = module_loader.loadFromDir(file, "app.src.listeners")

            listener_event_list = module().eventList()
            for event in listener_event_list.keys():
                event_list.append(event)

        eventDispatcher = EventDispatcher()
        eventDispatcher.init(list(set(event_list)))
        notifier = eventDispatcher.getDispatcher()

        index = 0
        priority_list = {}
        for file in glob(os.path.join(path, "*.py")):
            module = module_loader.loadFromDir(file, "app.src.listeners")

            listener_event_list = module().eventList()
            for event in listener_event_list.keys():
                if listener_event_list[event]["priority"] not in priority_list:
                    priority_list[listener_event_list[event]["priority"]] = {}

                listener_event_list[event]["event"] = event
                priority_list[listener_event_list[event]["priority"]][index] = listener_event_list[event]
                index += 1

        for priority in sorted(priority_list.keys()):
            for elem in priority_list[priority]:
                notifier.subscribe(priority_list[priority][elem]["event"], priority_list[priority][elem]["action"])