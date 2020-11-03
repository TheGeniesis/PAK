from EventNotifier import Notifier

from app.src.services.core.SingletonMeta import SingletonMeta


class EventDispatcher(metaclass=SingletonMeta):
    __notifier = None

    def getDispatcher(self):
        if self.__notifier is None:
            self.init([])

        return self.__notifier

    def init(self, event_list: list):
        self.__notifier = Notifier(event_list)
