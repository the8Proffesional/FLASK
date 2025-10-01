from extentions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"User('{self.name}', '{self.password}')"
    
class Arondissement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    arondissement = db.Column(db.String(25), unique=True, nullable=False)
    departement = db.relationship('Departement', backref='Departement', lazy=True)
    
    def __repr__(self):
        return f"Arondissement : {self.arondissement}"
    
class Departement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    departement = db.Column(db.String(25), unique=True, nullable=False)
    arondissement = db.Column(db.Integer, db.ForeignKey('arondissement.id'), nullable=False)

    def __repr__(self):
        return f"Departement : {self.departement} - Arondissement : {self.arondissement.arondissement}"