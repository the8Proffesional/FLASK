from flask import Blueprint, flash, render_template, redirect, url_for, request
from flask import session
from models import Arondissement, Departement, Utilisateur
from extentions import db   

utilisateur = Blueprint('utilisateur', __name__, template_folder='templates')


@utilisateur.route('/manage_Utilisateurs', methods=['GET', 'POST'])
def manage_Utilisateurs():
    arrondissements = Arondissement.query.all()
    if 'user' not in session:
        return redirect(url_for('admin.admin'))
    if request.method == 'POST':
        if 'arrondissementName' in request.form:
            arrondissement_id = request.form['arrondissementName']
            departements = Departement.query.filter_by(arondissement=arrondissement_id).all()
            return render_template('manage_Utilisateurs.html', name=session['user'], arrondissements=arrondissements, departements=departements, selected_arrondissement=int(arrondissement_id), selected_departement=-1)
        if 'departementName' in request.form:
            departement_id = request.form['departementName']
            arrondissement_id = request.form['arrondissementName1']
            departements = Departement.query.filter_by(arondissement=arrondissement_id).all()
            utilisateurs = Utilisateur.query.filter_by(departement=departement_id).all()
            return render_template('manage_Utilisateurs.html', name=session['user'], arrondissements=arrondissements, selected_arrondissement=int(arrondissement_id), departements=departements, selected_departement= int(departement_id), utilisateurs=utilisateurs)
        if 'utilisateurName' in request.form:
            departement_id = request.form['departementName1']
            NomUtilisateur = request.form['utilisateurName']
            arrondissement_id = request.form['arrondissementName2']
            departements = Departement.query.filter_by(arondissement=arrondissement_id).all()
            newUtilisateur = Utilisateur(nomUtilisateur=NomUtilisateur, departement=departement_id)
            db.session.add(newUtilisateur) 
            db.session.commit()
            utilisateurs = Utilisateur.query.filter_by(departement=departement_id).all()
            return render_template('manage_Utilisateurs.html', name=session['user'], arrondissements=arrondissements, departements=departements, selected_arrondissement=int(arrondissement_id), selected_departement=int(departement_id), utilisateurs=utilisateurs)
    
    return render_template('manage_Utilisateurs.html',  name=session['user'], arrondissements=arrondissements, selected_arrondissement=-1)


@utilisateur.route('/update_Utilisateur/<int:id>', methods=['GET', 'POST'])
def update_Utilisateur(id):
    if 'user' not in session:
        return redirect(url_for('admin.admin'))
    utilisateur = Utilisateur.query.get(id)
    departement = Departement.query.get(utilisateur.departement)
    arrondissement = Arondissement.query.get(departement.arondissement)
    if request.method == 'POST':
        utilisateur.nomUtilisateur = request.form['utilsateurName']
        db.session.commit()
        departements = Departement.query.filter_by(arondissement=arrondissement.id).all()
        return render_template('manage_Utilisateurs.html', arrondissements=Arondissement.query.all(), departements=departements, name=session['user'], selected_arrondissement=int(arrondissement.id), selected_departement=int(departement.id), utilisateurs=Utilisateur.query.filter_by(departement=departement.id).all())
    return render_template('update_utilisateur.html', name=session['user'], utilisateur=utilisateur, arrondissement=arrondissement, departement=departement)

@utilisateur.route('/delete_Utilisateur/<int:id>', methods=['GET'])
def delete_Utilisateur(id):
    if 'user' not in session:
        return redirect(url_for('admin.admin'))
    utilisateur = Utilisateur.query.get(id)
    departement = Departement.query.get(utilisateur.departement)
    arrondissement = Arondissement.query.get(departement.arondissement)
    departements = Departement.query.filter_by(arondissement=arrondissement.id).all()
    db.session.delete(utilisateur)
    db.session.commit()
    return render_template('manage_Utilisateurs.html', arrondissements=Arondissement.query.all(), departements=departements, name=session['user'], selected_arrondissement=int(arrondissement.id), selected_departement=int(departement.id), utilisateurs=Utilisateur.query.filter_by(departement=departement.id).all())