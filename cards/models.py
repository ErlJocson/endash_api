from dynamorm import DynamoModel, fields

class Cards(DynamoModel):

    class Table:
        name = "Cards"
        hash_key = "card_id"

    ID = fields.String(hash_key=True)
    title = fields.String()
    logo = fields.String()
    video = fields.String()
    link = fields.String()
    position = fields.Integer()
