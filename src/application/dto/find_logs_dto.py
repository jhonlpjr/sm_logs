from src.domain.interfaces.log_interface import ILog


class FindLogsDto :
        id: int
        prevStatus: object
        nextStatus: object
        request: object
        response: object
