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
        return f"Departement : {self.departement} - Arondissement : {self.arondissement}"
    
class Utilisateur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nomUtilisateur = db.Column(db.String(50), unique=True, nullable=False)
    departement = db.Column(db.Integer, db.ForeignKey('departement.id'), nullable=False)

    def __repr__(self):
        return f"Nom : {self.nomUtilisateur} - Departement : {self.departement}"
    
class MaterialType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    typeMaterial = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f"Type Material : {self.typeMaterial}"
    
class Marque(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    MarqueName = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f"Marque : {self.MarqueName}"

class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    modelname = db.Column(db.String(50), unique=True, nullable=False)
    type_material_id = db.Column(db.Integer, db.ForeignKey('material_type.id'), nullable=False)
    marque_id = db.Column(db.Integer, db.ForeignKey('marque.id'), nullable=False)
    support_uri = db.Column(db.String(200), unique=False, nullable=True)

    def __repr__(self):
        return f"Model : {self.modelname} - Type Material ID : {self.type_material_id} - Marque ID : {self.marque_id}"