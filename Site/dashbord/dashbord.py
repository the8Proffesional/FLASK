from flask import Blueprint, render_template, redirect, url_for
from flask import session

dashbord = Blueprint('dashbord', __name__, template_folder='templates')
@dashbord.route('/dashbord')
def dashbord_page():
    if 'user' not in session:
        return redirect(url_for('admin.admin'))    
    return render_template('dashbord.html', name=session['user'])