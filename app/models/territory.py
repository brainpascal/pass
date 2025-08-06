from app import db

class Territory(db.Model):
    __tablename__ = 'Territory'
    territoryId = db.Column(db.String(20), primary_key=True)
    territorydescription = db.Column(db.String(50), nullable=False)
    regionId = db.Column(db.Integer, db.ForeignKey('Region.regionId'), nullable=False)

    region = db.relationship('Region', backref='territories')

    def __repr__(self):
        return f'<Territory {self.territorydescription}>'
