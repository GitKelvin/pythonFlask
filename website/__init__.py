'''
packages "website folder" into a python package and can be imported outside of this folder

'''
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asdf asdf asdf'

    # importing the views from the Blueprint views
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    return app