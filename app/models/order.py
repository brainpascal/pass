from app import db

class SalesOrder(db.Model):
    __tablename__ = 'SalesOrder'
    orderId = db.Column(db.Integer, primary_key=True)
    custId = db.Column(db.Integer, db.ForeignKey('Customer.custId'), nullable=False)
    employeeId = db.Column(db.Integer)
    orderDate = db.Column(db.DateTime)
    requiredDate = db.Column(db.DateTime)
    shippedDate = db.Column(db.DateTime)
    shipperid = db.Column(db.Integer, db.ForeignKey('Shipper.shipperid'), nullable=False)
    freight = db.Column(db.Numeric(10, 2))
    shipName = db.Column(db.String(40))
    shipAddress = db.Column(db.String(60))
    shipCity = db.Column(db.String(15))
    shipRegion = db.Column(db.String(15))
    shipPostalCode = db.Column(db.String(10))
    shipCountry = db.Column(db.String(15))

    details = db.relationship('OrderDetail', backref='sales_order', cascade="all, delete-orphan")

class OrderDetail(db.Model):
    __tablename__ = 'OrderDetail'
    orderDetailId = db.Column(db.Integer, primary_key=True)
    orderId = db.Column(db.Integer, db.ForeignKey('SalesOrder.orderId'), nullable=False)
    productId = db.Column(db.Integer, db.ForeignKey('Product.productId'), nullable=False)
    unitPrice = db.Column(db.Numeric(10, 2), nullable=False)
    quantity = db.Column(db.SmallInteger, nullable=False)
    discount = db.Column(db.Numeric(10, 2), nullable=False)
