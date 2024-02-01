from marshmallow import Schema, fields

from src.application.dto.create_log_dto import CreateLogDto


class CreateLogSchema(Schema) :
    id = fields.String(required=True)
    prevStatus = fields.Raw(required=False)
    nextStatus = fields.Raw(required=False)
    request = fields.Raw(required=False)
    response = fields.Raw(required=False)
    
    def validates(self, data):
        errors = self.validate(data)
        if errors:
            raise Exception(errors)