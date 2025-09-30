from flask import Blueprint, render_template, redirect, url_for
from flask import session

about = Blueprint('about', __name__, template_folder='templates')
@about.route('/about')
def about_page():
    if 'user' not in session:
        return redirect(url_for('main.home'))    
    return render_template('about.html')