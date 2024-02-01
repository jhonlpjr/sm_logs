# app/use_cases.py

from src.infraestructure.providers.log_provider import LOG_REPOSITORY_PROVIDER
from src.domain.entities.log_entity import LogEntity
from src.domain.repository.log_repository import LogRepository

class FindOneLogUsecase:
    def __init__(self, collectionName: str):
        
        self.log_repository: LogRepository = LOG_REPOSITORY_PROVIDER(collectionName)
    
    def execute(self, id: int):
        # Lógica para buscar logs
        data = self.log_repository.findById(id)
        log = LogEntity(data)
        return log