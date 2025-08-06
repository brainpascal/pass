from app import db

class Supplier(db.Model):
    __tablename__ = 'Supplier'

    supplierId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    companyName = db.Column(db.String(40), nullable=False)
    contactName = db.Column(db.String(30))
    contactTitle = db.Column(db.String(30))
    address = db.Column(db.String(60))
    city = db.Column(db.String(15))
    region = db.Column(db.String(15))
    postalCode = db.Column(db.String(10))
    country = db.Column(db.String(15))
    phone = db.Column(db.String(24))
    email = db.Column(db.String(225))
    fax = db.Column(db.String(24))
    HomePage = db.Column(db.Text)
