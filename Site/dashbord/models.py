from flask import Blueprint, render_template, redirect, url_for, request
from flask import session
from models import Arondissement, Departement, MaterialType, Marque, Model, Utilisateur
from extentions import db   

ModelMaterial = Blueprint('model_material', __name__, template_folder='templates')


@ModelMaterial.route('/manage_Models', methods=['GET', 'POST'])
def manage_Models():
    if 'user' not in session:
        return redirect(url_for('adminstration.login')) 
    MaterialTypes = MaterialType.query.all()
    Marques = Marque.query.all()
    models = Model.query.all()
    if request.method == 'POST':
        selected_TypeMaterial = request.form.get('TypeName', type=int)
        selected_Marque = request.form.get('MarqueName', type=int)
        ModelName = request.form.get('ModelName')
        support = request.form.get('SupportName')
        
        
        new_model = Model(
            modelname=ModelName,
            type_material_id=selected_TypeMaterial,
            marque_id=selected_Marque,
            support_uri=support
        )
        db.session.add(new_model)
        db.session.commit()
        models = Model.query.all()
        return render_template('Manage_materials.html',  name=session['user'], TypeMaterials=MaterialTypes, Marques=Marques, models=models, submitted=True, selected_TypeMaterial=selected_TypeMaterial, selected_Marque=selected_Marque)
    return render_template('Manage_materials.html',  name=session['user'], TypeMaterials=MaterialTypes, Marques=Marques, models=models, submitted=False)

@ModelMaterial.route('/delete_Models/<int:model_id>', methods=['GET'])
def delete_model(model_id):
    model = Model.query.get_or_404(model_id)
    db.session.delete(model)
    db.session.commit()
    return redirect(url_for('model_material.manage_Models'))