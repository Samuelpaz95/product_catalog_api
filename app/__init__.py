from flask import Flask
from flask_login import LoginManager
from .views import page, db

APP = Flask(__name__)

login_manager = LoginManager()


def create_app(config) -> Flask:
    APP.config.from_object(config)
    APP.register_blueprint(page)
    login_manager.init_app(APP)
    db.config_engine(user=config.DATABASE_USER, password='')
    return APP
