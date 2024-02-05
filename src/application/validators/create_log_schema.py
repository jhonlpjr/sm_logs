from marshmallow import Schema, fields

class CreateLogSchema(Schema) :
    id = fields.String(required=True)
    operation = fields.String(required=True)
    prevStatus = fields.Raw(required=False)
    nextStatus = fields.Raw(required=False)
    request = fields.Raw(required=False)
    response = fields.Raw(required=False)
    status = fields.Boolean(required=False)
    createdBy = fields.Integer(required=False)
    
    def validates(self, data):
        errors = self.validate(data)
        if errors:
            raise Exception(errors)