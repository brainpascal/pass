from app import db

class Product(db.Model):
    __tablename__ = 'Product'

    productId = db.Column(db.Integer, primary_key=True)
    productName = db.Column(db.String(40), nullable=False)
    supplierId = db.Column(db.Integer)
    categoryId = db.Column(db.Integer)
    quantityPerUnit = db.Column(db.String(20))
    unitPrice = db.Column(db.Numeric(10, 2))
    unitsInStock = db.Column(db.SmallInteger)
    unitsOnOrder = db.Column(db.SmallInteger)
    reorderLevel = db.Column(db.SmallInteger)
    discontinued = db.Column(db.String(1), nullable=False)
