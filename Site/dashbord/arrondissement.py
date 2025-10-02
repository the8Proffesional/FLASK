from flask import Blueprint, render_template, redirect, url_for, request
from flask import session
from models import Arondissement
from extentions import db   

arrondissement = Blueprint('arrondissement', __name__, template_folder='templates')

@arrondissement.route('/manage_Arrondissements', methods=['GET', 'POST'])
def manage_Arrondissements():
    if 'user' not in session:
        return redirect(url_for('admin.admin'))
    if request.method == 'POST':
        arrondissement_name = request.form.get('arrondissementName')
        if arrondissement_name:
            new_arrondissement = Arondissement(arondissement=arrondissement_name)
            db.session.add(new_arrondissement)
            db.session.commit()
            return redirect(url_for('arrondissement.manage_Arrondissements')) 
        
    arrondissements = Arondissement.query.all() 

    return render_template('manage_Arrondissements.html', name=session['user'], arrondissements=arrondissements)

@arrondissement.route('/delete_arrondissement/<int:arrondissement_id>', methods=['POST'])
def delete_arrondissement(arrondissement_id):   
    if 'user' not in session:
        return redirect(url_for('admin.admin'))
    
    arrondissement = Arondissement.query.get_or_404(arrondissement_id)
    db.session.delete(arrondissement)
    db.session.commit()
    return redirect(url_for('arrondissement.manage_Arrondissements'))

@arrondissement.route('/update_arrondissement/<int:arrondissement_id>', methods=['GET', 'POST'])
def update_arrondissement(arrondissement_id):
    if 'user' not in session:
        return redirect(url_for('admin.admin'))
    
    arrondissement = Arondissement.query.get_or_404(arrondissement_id)
    
    if request.method == 'POST':
        new_name = request.form.get('arrondissementName')
        if new_name:
            arrondissement.arondissement = new_name
            db.session.commit()
            return redirect(url_for('arrondissement.manage_Arrondissements'))
    
    return render_template('update_arondissement.html', name=session['user'], arrondissement=arrondissement)