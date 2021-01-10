from flask import Blueprint
from flask import request
from flask.helpers import flash
from flask.json import jsonify
from flask_login import login_user
from flask_login import LoginManager
from flask_login.utils import logout_user
from .models import User
from .db_conncetion import db

page = Blueprint('page', __name__)
login_manager = LoginManager()

@login_manager.user_loader
def load_user(id):
    return db.get_by_id(User, id)

@page.route('/login', methods=['POST'])
def login():
    data:dict = request.get_json()
    if 'username' in data and 'password' in data:
        user:User = db.get_by(User, **{'username':data['username']})[0]
        if not user:
           return jsonify({"msg":"the username is incorrect"}) 
        if user.verify_password(data['password']):
            login_user(user)
            db.switch_to_admin()
            return jsonify(user.to_json())
        else:
            return jsonify({"msg":"the password is incorrect"})
    return jsonify({"msg":"the fields are incorrect"})

@page.route('/logout', methods=['GET'])
def logout():
    db.switch_to_anonymous()
    logout_user()
    return jsonify({"msg":"the session was closed"})