from flask import Flask
def create_app():
    app = Flask(__name__)
    app.config['SESSION_TYPE'] = 'memcached'
    app.config['SECRET_KEY'] = 'super secret key'
    #sess = Session()

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    return app
    