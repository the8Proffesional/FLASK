from flask import Blueprint, render_template
from flask import Blueprint, render_template, request, redirect, url_for
from models import Arondissement, Departement, Model, Utilisateur, Material

main = Blueprint('main', __name__)

@main.route('/')
def home():
    arrondissements = Arondissement.query.all()
    return render_template("index.html", arrondissements=arrondissements)

@main.route('/departements/', methods=['GET'])
def show_departements():
    arrondissements = Arondissement.query.all()
    if request.method == 'GET':
        dep_id=request.args.get('id', type=int)
        arr_id=request.args.get('arr_id', type=int)
        departements = Departement.query.filter_by(arondissement=dep_id).all()
        depa_id=request.args.get('depa_id', type=int)
        utilisateurs = Utilisateur.query.filter_by(departement=depa_id).all()
        user_id = request.args.get('user_id', type=int)
        materials = Material.query.filter_by(utilisateur_id=user_id).all()
        materialsListe =[]
        for mat in materials:
            materialsListe.append({"inventaire_number": mat.inventaire_number, "serial_number": mat.serial_number, "modelname": Model.query.get(mat.model_id).modelname})
        return render_template("index.html", arrondissements=arrondissements, departements=departements, id=dep_id, arr_id=arr_id, depa_id=depa_id, user_id=user_id, utilisateurs=utilisateurs, materials=materials, materialsListe=materialsListe)