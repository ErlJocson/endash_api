from dynamorm import DynamoModel, fields

class Cards(DynamoModel):
    id = fields.String(hash_key=True)
    title = fields.String()
    logo = fields.String()
    video = fields.String()
    link = fields.String()
    position = fields.Integer()
