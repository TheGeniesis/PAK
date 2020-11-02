from __future__ import annotations

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from app.src.services.core.config.Config import Config
from app.src.services.core.SingletonMeta import SingletonMeta


class BaseModel(metaclass=SingletonMeta):
    __declarative = None
    __connection = None
    __engine = None

    def getDeclarative(self):
        if self.__declarative is None:
            self.__declarative = declarative_base()

        return self.__declarative

    def getConnection(self):
        if self.__connection is None:
            engine = self.getEngine()
            self.__connection = engine.connect(check_same_thread=False)

        return self.__connection

    def getEngine(self):

        if self.__engine is None:
            config = Config()
            config = config.getConfig()
            self.__engine = create_engine(config["DATABASE"]["PATH"], echo=False)

        return self.__engine
