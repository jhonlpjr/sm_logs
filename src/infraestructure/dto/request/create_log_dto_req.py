from types import SimpleNamespace
from src.application.dto.create_log_dto import CreateLogDto
from src.application.validators.create_log_schema import CreateLogSchema


class CreateLogDtoReq(CreateLogDto) :

        def __init__(self, data_raw):
                
                if data_raw is None:
                    raise Exception('No data_raw for CreateLogDtoReq')
            
                schema = CreateLogSchema()
                schema.validates(data_raw)
                
                body:CreateLogDto  = SimpleNamespace(**data_raw)
                
                if(getattr(body, 'id', None)):
                    self.id = body.id
                if(getattr(body, 'prevStatus', None)):
                    self.prevStatus = body.prevStatus    
                if(getattr(body, 'nextStatus', None)):
                    self.nextStatus = body.nextStatus
                if(getattr(body, 'request', None)):
                    self.request = body.request
                if(getattr(body, 'response', None)):
                    self.response = body.response
                



