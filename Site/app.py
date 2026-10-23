from flask import  Flask
from dashbord.models import ModelMaterial
from main.main import main
from about.about import about
from admin.admin import adminstration
from dashbord.dashbord import dashbord
from dashbord.arrondissement import arrondissement
from dashbord.departement import departement
from dashbord.utilisateur import utilisateur
from dashbord.materialType import Material_Types
from dashbord.marques import Marques
from dashbord.material import material

from extentions import db
from models import User, OsVersions, Officeversions, Antivirus, MaterialType, Marque

from werkzeug.security import generate_password_hash

def createApp():

    app = Flask(__name__)
    app.secret_key = 'infoware'

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.register_blueprint(main)
    app.register_blueprint(about)
    app.register_blueprint(adminstration)
    app.register_blueprint(dashbord)
    app.register_blueprint(arrondissement)
    app.register_blueprint(departement)
    app.register_blueprint(utilisateur)
    app.register_blueprint(Material_Types)
    app.register_blueprint(Marques)
    app.register_blueprint(ModelMaterial)
    app.register_blueprint(material)

    

    db.init_app(app)
    TypesMaterial = [
        "Ordinateur Portable",
        "Ordinateur de Bureau",
        "Imprimante Laser B/W",
        "Imprimante Laser Couleur",
        "Scanner",
        "Onduleur",
    ]
    Material_Marques = [
        "HP",
        "Dell",
        "Lenovo",
        "Acer",
        "Epson",
        "Canon",
        "Samsung",
    ]




    os_versions = [
        "Windows 11",
        "Windows 10",
        "Windows 8.1",
        "Windows 7"
    ]
    
    office_versions = [
        "Microsoft Office 2010",
        "Microsoft Office 2013",
        "Microsoft Office 2016",
        "Microsoft Office 2019",
        "Microsoft Office 2021",
    ]
    
    antivirus_versions = [
        "Kaspersky Enddpoint Security",
        "Kaspersky Internet Security Plus",
        "Other...",
    ]

    with app.app_context():
        db.create_all()
        db.session.commit()


        for type_material in TypesMaterial:
            if not MaterialType.query.filter_by(typeMaterial=type_material).first():
                db.session.add(MaterialType(typeMaterial=type_material))
                db.session.commit()
        for marque in Material_Marques:
            if not Marque.query.filter_by(MarqueName=marque).first():
                db.session.add(Marque(MarqueName=marque))
                db.session.commit()



        for version in os_versions:
            if not OsVersions.query.filter_by(os_version=version).first():
                db.session.add(OsVersions(os_version=version))
                db.session.commit()

        for version in office_versions:
            if not Officeversions.query.filter_by(office_version=version).first():
                db.session.add(Officeversions(office_version=version))
                db.session.commit()

        for version in antivirus_versions:
            if not Antivirus.query.filter_by(antivirus_name=version).first():
                db.session.add(Antivirus(antivirus_name=version))
                db.session.commit()

        user = User(name='adil', password=generate_password_hash('infoware'))
        if not User.query.filter_by(name='adil').first():
            db.session.add(user)
            db.session.commit()
        
    return app

if __name__ == '__main__':
    createApp().run(debug=True)