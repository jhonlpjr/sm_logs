# app/use_cases.py

from types import SimpleNamespace
from datetime import datetime
from flask import json
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
        log.createdAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Formatear la fecha como cadena de texto
        dataLog = self.log_repository.save(log.__dict__)
        dataLog["_id"] = str(dataLog["_id"]) 
        resLog = json.dumps(dataLog)
        return resLog