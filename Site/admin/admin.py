from flask import Blueprint, render_template, request, redirect, url_for
from models import User
from werkzeug.security import check_password_hash
from flask import session

adminstration = Blueprint('admin', __name__)


@adminstration.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        username = request.form.get('name')
        password = request.form.get('pw')
        user = User.query.filter_by(name=username).first()
        if user and check_password_hash(user.password  , password):
            session['user'] = user.name
            return redirect(url_for('dashbord.dashbord_page'))    
    return render_template("admin.html")                       
    
@adminstration.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('admin')
