from flask import Blueprint, render_template, redirect, url_for, request
from flask import session
from models import MaterialType
from extentions import db   

Material_Types = Blueprint('materialTypes', __name__, template_folder='templates')

@Material_Types.route('/manage_MaterialTypes', methods=['GET', 'POST'])
def manage_MaterialTypes():
    if 'user' not in session:
        return redirect(url_for('admin.admin'))
    if request.method == 'POST':
        if 'materialTypeName' in request.form:
            materialTypeName = request.form['materialTypeName']
            newMaterialType = MaterialType(typeMaterial=materialTypeName)
            db.session.add(newMaterialType) 
            db.session.commit()
            materialTypes = MaterialType.query.all()
            return render_template('manage_MaterialTypes.html', name=session['user'], materialTypes=materialTypes)
    materialTypes = MaterialType.query.all()
    return render_template('manage_MaterialTypes.html',  name=session['user'], materialTypes=materialTypes)