# app/use_cases.py

from abc import abstractmethod
from types import SimpleNamespace

from flask import json
from src.infraestructure.database.repositories.log_mongodb_repository import LogMongoDBRepository
from src.infraestructure.providers.log_provider import LOG_REPOSITORY_PROVIDER
from src.domain.entities.log_entity import LogEntity
from src.domain.interfaces.log_interface import ILog
from src.domain.repository.log_repository import LogRepository
from src.infraestructure.database.config.adapter_mongodb import MongoDBAdapter

class FindLogsUsecase:
    
    def __init__(self, collectionName: str):
        self.log_repository: LogRepository = LOG_REPOSITORY_PROVIDER(collectionName)
        
    def execute(self, logFilters: any):
        # Lógica para buscar logs
        data = self.log_repository.findAll(logFilters)
        logs = [LogEntity(SimpleNamespace(**element)) for element in data]
        resLogs = [obj.__dict__ for obj in logs]
        return resLogs