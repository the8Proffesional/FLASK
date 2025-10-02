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



