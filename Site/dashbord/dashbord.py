from flask import Blueprint, render_template, redirect, url_for, request
from flask import session
from models import Arondissement
from extentions import db   

dashbord = Blueprint('dashbord', __name__, template_folder='templates')
@dashbord.route('/dashbord')
def dashbord_page():
    if 'user' not in session:
        return redirect(url_for('admin.admin'))    
    return render_template('dashbord.html', name=session['user'])

@dashbord.route('/manage_users')
def manage_users():
    if 'user' not in session:
        return redirect(url_for('admin.admin'))    
    return render_template('manage_users.html', name=session['user'])

@dashbord.route('/manage_Arrondissements', methods=['GET', 'POST'])
def manage_Arrondissements():
    if 'user' not in session:
        return redirect(url_for('admin.admin'))
    if request.method == 'POST':
        arrondissement_name = request.form.get('arrondissementName')
        if arrondissement_name:
            new_arrondissement = Arondissement(arondissement=arrondissement_name)
            db.session.add(new_arrondissement)
            db.session.commit()
            return redirect(url_for('dashbord.manage_Arrondissements')) 
        
    arrondissements = Arondissement.query.all() 

    return render_template('manage_Arrondissements.html', name=session['user'], arrondissements=arrondissements)

@dashbord.route('/delete_arrondissement/<int:arrondissement_id>', methods=['POST'])
def delete_arrondissement(arrondissement_id):   
    if 'user' not in session:
        return redirect(url_for('admin.admin'))
    
    arrondissement = Arondissement.query.get_or_404(arrondissement_id)
    db.session.delete(arrondissement)
    db.session.commit()
    return redirect(url_for('dashbord.manage_Arrondissements'))    