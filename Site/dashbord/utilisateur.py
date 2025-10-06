from flask import Blueprint, render_template, redirect, url_for, request
from flask import session
from models import Arondissement, Departement, Utilisateur
from extentions import db   

utilisateur = Blueprint('utilisateur', __name__, template_folder='templates')


@utilisateur.route('/manage_Utilisateurs', methods=['GET', 'POST'])
def manage_Utilisateurs():
    arrondissements = Arondissement.query.all()
    if 'user' not in session:
        return redirect(url_for('admin.admin'))
    departements=[]
    if request.method == 'POST':
        arrondissement_id = request.form['arrondissementName']
        departements = Departement.query.filter_by(arondissement=arrondissement_id).all()
        if 'departementName' in request.form:
            departement_id = int(request.form['departementName'])
            departements = Departement.query.filter_by(arondissement=arrondissement_id).all()
            return render_template('manage_Utilisateurs.html', name=session['user'], arrondissements=arrondissements, departements=departements, selected_arrondissement=int(arrondissement_id), selected_departement=int(departement_id))
        else:
            return render_template('manage_Utilisateurs.html', name=session['user'], arrondissements=arrondissements, departements=departements, selected_arrondissement=int(arrondissement_id), selected_departement=-1)
        
    return render_template('manage_Utilisateurs.html', name=session['user'], arrondissements=arrondissements, selected_arrondissement=-1)