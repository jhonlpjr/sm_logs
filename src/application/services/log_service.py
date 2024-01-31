# app/use_cases.py

from application.usecases.find_logs_usecase import FindLogsUsecase
from application.usecases.find_one_log_usecase import FindOneLogUsecase
from domain.interfaces.log_interface import ILog
from application.usecases.create_log_usecase import CreateLogUsecase

class LogService:
    def __init__(self, collectionName: str):
        
        self.create_log_usecase = CreateLogUsecase(collectionName)
        self.find_logs_usecase = FindLogsUsecase(collectionName)
        self.find_one_log_usecase = FindOneLogUsecase(collectionName)
    
    def create(self, log: ILog, createdBy: int):
        # Lógica para guardar el log en la base de datos MongoDB
        logCreated = self.create_log_usecase.execute(log, createdBy)
        return logCreated
    
    def findAll(self, log: ILog):
        # Lógica para obtener los logs de la base de datos MongoDB
        logs = self.find_logs_usecase.execute(log)
        return logs
    
    def findById(self, id: int):
        # Lógica para obtener un log por id de la base de datos MongoDB
        log = self.find_one_log_usecase.execute(id)
        return log