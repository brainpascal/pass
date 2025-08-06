from app.models.supplier import Supplier
from app import db

def get_all():
    return Supplier.query.all()

def get_by_id(id):
    return Supplier.query.get(id)

def create(data):
    new_supplier = Supplier(
        name=data['name'],
        contact_name=data['contact_name'],
        address=data['address'],
        city=data['city'],
        postal_code=data['postal_code'],
        country=data['country'],
        phone=data['phone']
    )
    db.session.add(new_supplier)
    db.session.commit()

def update(id, data):
    supplier = Supplier.query.get(id)
    supplier.name = data['name']
    supplier.contact_name = data['contact_name']
    supplier.address = data['address']
    supplier.city = data['city']
    supplier.postal_code = data['postal_code']
    supplier.country = data['country']
    supplier.phone = data['phone']
    db.session.commit()

def delete(id):
    supplier = Supplier.query.get(id)
    db.session.delete(supplier)
    db.session.commit()
