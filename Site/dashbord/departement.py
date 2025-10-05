from flask import Blueprint, render_template, redirect, url_for, request
from flask import session
from models import Arondissement, Departement
from extentions import db   

departement = Blueprint('departement', __name__, template_folder='templates')

@departement.route('/manage_Departements', methods=['GET', 'POST'])
def manage_Departements():
    if 'user' not in session:
        return redirect(url_for('admin.admin'))
    if request.method == 'POST':
        arrondissement_id = request.form['arrondissementName']
        departement_name = request.form['departementName']
        if departement_name != '':
            new_departement = Departement(departement=departement_name, arondissement=arrondissement_id)
            db.session.add(new_departement)
            db.session.commit() 
    else:
        arrondissement_id = -1   
    arrondissements = Arondissement.query.all()
    departements = Departement.query.filter_by(arondissement=arrondissement_id).all()
    return render_template('manage_Departements.html', name=session['user'], departements=departements, arrondissements=arrondissements, selected_arrondissement=int(arrondissement_id))
    

@departement.route('/delete_departement/<int:departement_id>', methods=['GET', 'POST'])
def delete_departement2(departement_id):   
    if 'user' not in session:
        return redirect(url_for('admin.admin'))
    arrond_id = Departement.query.get_or_404(departement_id).arondissement
    departement = Departement.query.get_or_404(departement_id)
    db.session.delete(departement)
    db.session.commit()
    arrondissements = Arondissement.query.all()
    departements = Departement.query.filter_by(arondissement=arrond_id).all()
    return render_template('manage_Departements.html', name=session['user'], departements=departements, arrondissements=arrondissements, selected_arrondissement=arrond_id)


@departement.route('/delete_departement/<int:departement_id>', methods=['GET', 'POST'])
def delete_departement(departement_id):   
    if 'user' not in session:
        return redirect(url_for('admin.admin'))
    departement = Departement.query.get_or_404(departement_id)
    db.session.delete(departement)
    db.session.commit()
    return redirect(url_for('arrondissement.update_arrondissement', arrondissement_id=departement.arondissement))