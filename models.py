from dbInit import db
from maInit import ma

class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique=True)
    descr = db.Column(db.String(100))
    price = db.Column(db.String(100))
    qty = db.Column(db.String(100))

    def __init__(self, name, descr, price, qty):
        self.name = name
        self.descr = descr
        self.price = price
        self.qty = qty


class ItemSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'descr', 'price', 'qty')

item_schema = ItemSchema()
items_schema = ItemSchema(many = True)

# db.create_all()