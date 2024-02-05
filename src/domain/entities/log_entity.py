from dataclasses import dataclass
from src.domain.interfaces.log_interface import ILog

@dataclass
class LogEntity(ILog):
    def __init__(self, partial_log: ILog):
        
        if partial_log is None:
            raise Exception('No data_log for LogEntity')
        
        if getattr(partial_log, 'id', None):
            self.id = partial_log.id
            
        if getattr(partial_log, 'operation', None):
            self.operation = partial_log.operation
        
        if getattr(partial_log, 'prevStatus', None):
            self.prevStatus = partial_log.prevStatus
            
        if getattr(partial_log, 'nextStatus', None):
            self.nextStatus = partial_log.nextStatus
        
        if getattr(partial_log, 'request', None):
            self.request = partial_log.request

        if getattr(partial_log, 'response', None):
            self.response = partial_log.response
            
        if getattr(partial_log, 'status', None):
            self.status = partial_log.status

        if getattr(partial_log, 'createdAt', None):
            self.createdAt = partial_log.createdAt
        
        if getattr(partial_log, 'updatedAt', None):
            self.updatedAt = partial_log.updatedAt
        
        if getattr(partial_log, 'deletedAt', None):
            self.deletedAt = partial_log.deletedAt
        
        if getattr(partial_log, 'createdBy', None):
            self.createdBy = partial_log.createdBy
        