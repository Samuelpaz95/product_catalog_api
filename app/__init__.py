from datetime import timedelta
from flask import Flask
from flask import jsonify
from flask.globals import session
from flask_restful import Api

from .products import ProductListResource, ProductResource
from .users import UserListResource, UserResource
from .common.error_handling import AppErrorBaseClass, ObjectNotFound
from .common import resource_bp
from .views import page, login_manager
from .db_conncetion import db

APP = Flask(__name__)
api = Api(resource_bp)

def create_app(config) -> Flask:
    APP.config.from_object(config)

    APP.register_blueprint(resource_bp)
    APP.register_blueprint(page)

    Api(APP, catch_all_404s=True)

    db.init_app(APP)
    login_manager.init_app(APP)
    login_manager.needs_refresh_message = (u"Session timedout, please re-login")
    login_manager.needs_refresh_message_category = "info"

    
    init_resources(api)
    if config.DEBUG:
        register_error_handlers(APP)
    return APP

@APP.before_request
def before_request():
    session.permanent = True
    APP.permanent_session_lifetime = timedelta(minutes=1)

def init_resources(api):
    api.add_resource(ProductListResource, '/api/products/')
    api.add_resource(ProductResource, '/api/products/<int:element_ID>')
    api.add_resource(UserListResource, '/api/users/')
    api.add_resource(UserResource, '/api/users/<int:element_ID>')


def register_error_handlers(app:Flask):
    @app.errorhandler(Exception)
    def handle_exception_error(error):
        print(error)
        return jsonify({'msg': 'Internal server error'}), 500
    @app.errorhandler(405)
    def handle_405_error(error):
        return jsonify({'msg': 'Method not allowed'}), 405
    @app.errorhandler(403)
    def handle_403_error(error):
        return jsonify({'msg': 'Forbidden error'}), 403
    @app.errorhandler(404)
    def handle_404_error(error):
        return jsonify({'msg': 'Not Found error'}), 404
    @app.errorhandler(AppErrorBaseClass)
    def handle_app_base_error(error):
        return jsonify({'msg': str(error)}), 500
    @app.errorhandler(ObjectNotFound)
    def handle_object_not_found_error(error):
        return jsonify({'msg': str(error)}), 404

