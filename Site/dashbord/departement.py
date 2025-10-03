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