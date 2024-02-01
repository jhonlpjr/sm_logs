from abc import ABC, abstractmethod
from typing import Any
from src.domain.interfaces.log_interface import ILog


class LogRepository(ABC):
    
    collectionName: str
    
    @abstractmethod
    def save(self, log: dict[ILog, Any]) -> dict[ILog, Any]:
        pass
    
    @abstractmethod
    def findById(self, id: int) -> dict[ILog, Any]:
        pass
    
    @abstractmethod
    def findAll(self, query: dict) -> list[dict[ILog, Any]]:
        pass