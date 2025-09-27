from flask import Blueprint
main = Blueprint('main', __name__)
from flask import render_template

@main.route('/')
def home():
    return render_template("index.html")