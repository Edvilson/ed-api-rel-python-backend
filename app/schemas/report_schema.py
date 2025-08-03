from marshmallow import Schema, fields

class ReportSchema(Schema):
    id = fields.Int(required=True)
    nome = fields.Str(required=True)
    data_evento = fields.Date(required=True)
    valor = fields.Float(required=True)
