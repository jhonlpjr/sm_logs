from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional

class ILog(ABC):
    
    id: str
    
    prevStatus: object

    nextStatus: object

    request: object

    response: object
    
    status: bool

    createdAt: datetime

    updatedAt: datetime

    deletedAt: datetime

    createdBy: int