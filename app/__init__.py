from flask import Flask
from .views import page

APP = Flask(__name__)

def create_app(config) -> Flask:
    APP.config.from_object(config)
    APP.register_blueprint(page)
    return APP
