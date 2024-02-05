from src.domain.interfaces.log_interface import ILog
from typing import Optional

class CreateLogDto :
        id: str
        operation: str
        prevStatus: Optional[object]
        nextStatus: object
        request: Optional[object]
        response: Optional[object]
        createdBy: Optional[int]
        status: Optional[bool]
