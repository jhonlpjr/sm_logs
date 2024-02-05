from src.domain.interfaces.log_interface import ILog


class FindLogsDto :
        id: int
        operation: str
        prevStatus: object
        nextStatus: object
        request: object
        response: object
