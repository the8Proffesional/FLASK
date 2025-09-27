from flask import  Flask, render_template, url_for
from main.main import main
from about.about import about

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(main, url_prefix='/home')
    app.register_blueprint(about, url_prefix='/about')
    @app.route('/')
    def home():
        return render_template("index.html")
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True) 