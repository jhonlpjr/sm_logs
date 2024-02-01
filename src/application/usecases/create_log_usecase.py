# app/use_cases.py

from src.application.dto.create_log_dto import CreateLogDto
from src.infraestructure.providers.log_provider import LOG_REPOSITORY_PROVIDER
from src.domain.entities.log_entity import LogEntity
from src.domain.interfaces.log_interface import ILog
from src.domain.repository.log_repository import LogRepository

class CreateLogUsecase:
    def __init__(self, collectionName: str):
        self.log_repository: LogRepository = LOG_REPOSITORY_PROVIDER(collectionName)
    
    def execute(self, log: CreateLogDto, createdBy: int):
        # Lógica para guardar el log en la base de datos MongoDB
        log.createdBy = createdBy
        data = self.log_repository.save(log)
        logCreated = LogEntity(data)
        return logCreated