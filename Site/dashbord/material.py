from pyexpat import model

from flask import Blueprint, render_template, redirect, url_for, request
from flask import session
from models import   Marque, MaterialType, Material, Model, Utilisateur
from extentions import db   


material = Blueprint('material', __name__, template_folder='templates')

@material.route('/manage_Materials', methods=['GET', 'POST'])
def manage_Materials():
    if 'user' not in session:
        return redirect(url_for('adminstration.login')) 
    materials = Material.query.all()
    models = Model.query.all()
    utilisateurs = Utilisateur.query.all()
    modelList=[]
    for material in materials:
        model = Model.query.get(material.model_id)
        MaterialTypeName = MaterialType.query.get(model.type_material_id)
        marqueName = Marque.query.get(model.marque_id)
        user_name = Utilisateur.query.get(material.utilisateur_id)
        modelList.append([material, model.modelname, MaterialTypeName.typeMaterial, marqueName.MarqueName, user_name.nomUtilisateur])


    if request.method == 'POST':
        inventaire_number = request.form.get('ort')
        SerialNumber = request.form.get('sn')
        Model_id = request.form.get('ModelId', type=int)
        user_id = request.form.get('UserId', type=int)
        
        
        newMaterial = Material(
            serial_number=SerialNumber,
            inventaire_number=inventaire_number,
            model_id=Model_id,
            utilisateur_id=user_id
        )
        db.session.add(newMaterial)
        db.session.commit() 
        materials = Material.query.all()
        modelList=[]
        for material in materials:
            model = Model.query.get(material.model_id)
            MaterialTypeName = MaterialType.query.get(model.type_material_id)
            marqueName = Marque.query.get(model.marque_id)
            user_name = Utilisateur.query.get(material.utilisateur_id)
            modelList.append([material, model.modelname, MaterialTypeName.typeMaterial, marqueName.MarqueName, user_name.nomUtilisateur])
        

        return render_template('Manage_Material.html',  name=session['user'], materials=materials, submitted=True, models=models, utilisateurs=utilisateurs, selected_Model=Model_id, selected_User=user_id, list=modelList)
    return render_template('Manage_Material.html',  name=session['user'], materials=materials, models=models, utilisateurs=utilisateurs, submitted=False, list=modelList)

@material.route('/update_material/<int:material_id>', methods=['GET', 'POST'])
def update_material(material_id):
    if 'user' not in session:
        return redirect(url_for('adminstration.login')) 
    material = Material.query.get_or_404(material_id)
    models = Model.query.all()
    utilisateurs = Utilisateur.query.all()
    userid= Utilisateur.query.get(material.utilisateur_id).id
    if request.method == 'POST':
        material.inventaire_number = request.form.get('ort')
        material.serial_number = request.form.get('sn')
        material.model_id = request.form.get('ModelId', type=int)
        material.utilisateur_id = request.form.get('UserId', type=int)
        db.session.commit() 
        return redirect(url_for('material.manage_Materials'))
    return render_template('update_selected_material.html', name=session['user'], material=material, models=models, utilisateurs=utilisateurs, selected_Model=material.model_id, selected_User=userid)


@material.route('/delete_material/<int:material_id>', methods=['GET'])
def delete_material(material_id):
    if 'user' not in session:
        return redirect(url_for('adminstration.login')) 
    material = Material.query.get(material_id)
    if material:
        db.session.delete(material)
        db.session.commit()
    return redirect(url_for('material.manage_Materials'))