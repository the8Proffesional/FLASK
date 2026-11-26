from flask import Blueprint, render_template
from flask import Blueprint, render_template, request, redirect, url_for
from models import Arondissement, Departement, Model, Utilisateur, Material, Marque, MaterialType, OsVersions, Officeversions, Antivirus


main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def home():
    arrondissements = Arondissement.query.all()
    user_id=None
    user=None
    Materials = []
    if request.method=='POST':
        user_id=request.form.get('utilisateur_id')
        user=Utilisateur.query.filter_by(id=user_id).first()
    
        materialsListe = Material.query.filter_by(utilisateur_id=user_id).all()
        
        for m in materialsListe: 
            model=Model.query.filter_by(id=m.model_id).first()
            type= MaterialType.query.filter_by(id=model.type_material_id).first()
            marque = Marque.query.filter_by(id=model.marque_id).first()
            mat={'id': m.id, 'inventaire_number' : m.inventaire_number,'serial_number': m.serial_number, 'modelname' : model.modelname, 'typeMaterial' :type.typeMaterial,'MarqueName' : marque.MarqueName }

            Materials.append(mat)
    return render_template("index.html", arrondissements=arrondissements, user=user, Materials=Materials)

@main.route('/departements/', methods=['GET'])
def show_departements():
    arrondissements = Arondissement.query.all()
    id = request.args.get('id')
    Materials = []
    departements = Departement.query.filter_by(arondissement=id).all()
    dep_id = request.args.get('depa_id')
    utilisateurs = Utilisateur.query.filter_by(departement=dep_id).all()
    user_id=request.args.get('user_id')
    user=Utilisateur.query.filter_by(id=user_id).first()
    materialsListe = Material.query.filter_by(utilisateur_id=user_id).all()
            
    for m in materialsListe: 
        model=Model.query.filter_by(id=m.model_id).first()
        type= MaterialType.query.filter_by(id=model.type_material_id).first()
        marque = Marque.query.filter_by(id=model.marque_id).first()
        mat={'id': m.id, 'inventaire_number' : m.inventaire_number,'serial_number': m.serial_number, 'modelname' : model.modelname, 'typeMaterial' :type.typeMaterial,'MarqueName' : marque.MarqueName }

        Materials.append(mat)

    print(id)
    return render_template("index.html", arrondissements=arrondissements, departements=departements, utilisateurs=utilisateurs, user=user, Materials=Materials)

@main.route('/detail_material/<int:material_id>', methods=['GET'])
def detail_material(material_id):
    material = Material.query.get_or_404(material_id)
    model = Model.query.get(material.model_id)
    type_material = MaterialType.query.get(model.type_material_id)
    marque = Marque.query.get(model.marque_id)
    utilisateur = Utilisateur.query.get(material.utilisateur_id)
    departement = Departement.query.get(utilisateur.departement)
    arrondissement = Arondissement.query.get(departement.arondissement)
    
    os_version = OsVersions.query.get(material.os_version_id) if material.os_version_id else None
    office_version = Officeversions.query.get(material.office_version_id) if material.office_version_id else None
    antivirus = Antivirus.query.get(material.antivirus_id) if material.antivirus_id else None
    
    
    
    return render_template('detailmaterial.html', 
                           material=material, 
                           model=model, 
                           type_material=type_material, 
                           marque=marque, 
                           utilisateur=utilisateur, 
                           departement=departement, 
                           arrondissement=arrondissement,
                           os_version=os_version,
                           office_version=office_version,
                           antivirus=antivirus)