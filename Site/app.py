from flask import  Flask, url_for
from main.main import main
from about.about import about
from admin.admin import adminstration
from extentions import db

def createApp():
    app = Flask(__name__)
    app.secret_key = 'infoware'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.register_blueprint(main)
    app.register_blueprint(about)
    app.register_blueprint(adminstration)
    db.init_app(app)


    return app
    

if __name__ == '__main__':
    createApp().run(debug=True)