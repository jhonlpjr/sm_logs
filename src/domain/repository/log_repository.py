from abc import ABC, abstractmethod

from src.domain.interfaces.log_interface import ILog


class LogRepository(ABC):
    
    collectionName: str
    
    @abstractmethod
    def save(self, log: ILog) -> ILog:
        pass
    
    @abstractmethod
    def findById(self, id: int) -> ILog:
        pass
    
    @abstractmethod
    def findAll(self, query: ILog) -> list[ILog]:
        pass