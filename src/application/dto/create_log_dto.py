from src.domain.interfaces.log_interface import ILog


class CreateLogDto :
        id: int
        prevStatus: object
        nextStatus: object
        request: object
        response: object
