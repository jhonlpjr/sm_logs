# app/use_cases.py

import logging
from types import SimpleNamespace
from datetime import datetime
from flask import json
from src.application.dto.create_log_dto import CreateLogDto
from src.infraestructure.providers.log_provider import LOG_REPOSITORY_PROVIDER
from src.domain.entities.log_entity import LogEntity
from src.domain.interfaces.log_interface import ILog
from src.domain.repository.log_repository import LogRepository


logger = logging.getLogger()
logger.setLevel(logging.INFO)
class CreateLogUsecase:
    def __init__(self, collectionName: str):
        self.log_repository: LogRepository = LOG_REPOSITORY_PROVIDER(collectionName)
    
    def execute(self, log: CreateLogDto):
        # Lógica para guardar el log en la base de datos MongoDB
        try:
            logger.info("CreateLogUsecase | entrando bien: " + str(log.__dict__))
            log.createdAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Formatear la fecha como cadena de texto
            dataLog = self.log_repository.save(log.__dict__)
            dataLog["_id"] = str(dataLog["_id"]) 
            resLog = dataLog
            return resLog
        except Exception as e:
            logger.error("CreateLogUsecase | Error: " + str(e))
            raise e