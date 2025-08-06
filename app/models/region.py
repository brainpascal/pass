from app import db

class Region(db.Model):
    __tablename__ = 'Region'
    regionId = db.Column(db.Integer, primary_key=True)
    regiondescription = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Region {self.regiondescription}>'
