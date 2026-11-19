from flask import Blueprint, render_template
from flask import Blueprint, render_template, request, redirect, url_for
from models import Arondissement, Departement, Model, Utilisateur, Material, Marque, MaterialType

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
            mat={'inventaire_number' : m.inventaire_number,'serial_number': m.serial_number, 'modelname' : model.modelname, 'typeMaterial' :type.typeMaterial,'MarqueName' : marque.MarqueName }
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
        mat={'inventaire_number' : m.inventaire_number,'serial_number': m.serial_number, 'modelname' : model.modelname, 'typeMaterial' :type.typeMaterial,'MarqueName' : marque.MarqueName }
        Materials.append(mat)

    print(id)
    return render_template("index.html", arrondissements=arrondissements, departements=departements, utilisateurs=utilisateurs, user=user, Materials=Materials)