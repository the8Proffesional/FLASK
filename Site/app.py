from flask import  Flask
from main.main import main
from about.about import about
from admin.admin import adminstration
from dashbord.dashbord import dashbord
from dashbord.arrondissement import arrondissement
from extentions import db
from models import User

def createApp():
    app = Flask(__name__)
    app.secret_key = 'infoware'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.register_blueprint(main)
    app.register_blueprint(about)
    app.register_blueprint(adminstration)
    app.register_blueprint(dashbord)
    app.register_blueprint(arrondissement)

    db.init_app(app)
    from werkzeug.security import generate_password_hash

    with app.app_context():
        db.create_all()
        user = User(name='adil', password=generate_password_hash('infoware'))

        if not User.query.filter_by(name='adil').first():
            db.session.add(user)
            db.session.commit() 

    
    return app
    

if __name__ == '__main__':
    createApp().run(debug=True)