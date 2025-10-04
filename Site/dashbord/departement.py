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
        arrondissement=request.form['arrondissementName']
        departement_name = request.form['departementName']
        #arrond = Arondissement.query.get(arrondissement)
        new_departement = Departement(departement=departement_name, arondissement=arrondissement)
        db.session.add(new_departement)
        db.session.commit()
        return redirect(url_for('departement.manage_Departements'))
        
    arrondissements = Arondissement.query.all() 

    return render_template('manage_Departements.html', name=session['user'], arrondissements=arrondissements)


@departement.route('/delete_departement/<int:departement_id>', methods=['GET', 'POST'])
def delete_departement(departement_id):   
    if 'user' not in session:
        return redirect(url_for('admin.admin'))
    departement = Departement.query.get_or_404(departement_id)
    db.session.delete(departement)
    db.session.commit()
    return redirect(url_for('arrondissement.update_arrondissement', arrondissement_id=departement.arondissement))