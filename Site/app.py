from flask import  Flask, render_template, url_for
from main.main import main
from about.about import about

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(main)
    app.register_blueprint(about)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True) 