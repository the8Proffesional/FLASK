from flask import Blueprint, render_template, redirect, url_for, request
from flask import session
from models import Marque
from extentions import db   

Marques = Blueprint('marques', __name__, template_folder='templates')

@Marques.route('/manage_Marques', methods=['GET', 'POST'])
def manage_Marques():
    if 'user' not in session:
        return redirect(url_for('admin.admin'))
    if request.method == 'POST':
        if 'Marque' in request.form:
            Marqu = request.form['Marque']
            newMarque = Marque(MarqueName=Marqu)
            db.session.add(newMarque) 
            db.session.commit()
            Marques = Marque.query.all()
            return render_template('manage_Marques.html', name=session['user'], Marques=Marques)
    Marques = Marque.query.all()
    return render_template('manage_Marques.html',  name=session['user'], Marques=Marques)

@Marques.route('/update_Marque/<int:Marque_id>', methods=['GET', 'POST'])
def update_Marque(Marque_id):   
    if 'user' not in session:
        return redirect(url_for('admin.admin'))
    mod_Marque = Marque.query.get_or_404(Marque_id)
    if request.method == 'POST':
        if 'MarqueName' in request.form:
            MarqueName = request.form['MarqueName']
            mod_Marque.MarqueName = MarqueName
            db.session.commit()
            return redirect(url_for('marques.manage_Marques'))
    return render_template('update_Marques.html', name=session['user'], Marque=mod_Marque)


@Marques.route('/delete_Marque/<int:Marque_id>', methods=['GET'])
def delete_Marque(Marque_id):
    if 'user' not in session:
        return redirect(url_for('admin.admin'))
    del_Marque = Marque.query.get_or_404(Marque_id)
    db.session.delete(del_Marque)
    db.session.commit()
    return redirect(url_for('marques.manage_Marques'))