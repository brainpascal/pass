from app import db

class Category(db.Model):
    __tablename__ = 'Category'
    categoryId = db.Column(db.Integer, primary_key=True)
    categoryName = db.Column(db.String(15), nullable=False)
    description = db.Column(db.Text)
    picture = db.Column(db.LargeBinary)

