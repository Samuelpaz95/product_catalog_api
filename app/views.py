from flask import Blueprint
from flask import request, session, jsonify
from flask_login import LoginManager
from flask_login import login_user, logout_user
from .models import User
from .db_conncetion import db

page = Blueprint('page', __name__)
login_manager = LoginManager()

@login_manager.user_loader
def load_user(id):
    return db.get_by_id(User, id)

@page.route('/', methods=['GET'])
def index():
    return '<h2>Welcome to Catalog API</h2><br><a href="https://github.com/Samuelpaz95/product_catalog_api/blob/master/doc/api_doc.md">doc</a>'

@page.route('/login', methods=['POST'])
def login():
    data:dict = request.get_json()
    if 'username' in data and 'password' in data:
        user = db.get_by(User, **{'username':data['username']})
        if not user:
            return jsonify({"msg":"the username is incorrect"})
        user = user[0]
        if user.verify_password(data['password']):
            login_user(user)
            return jsonify(user.to_json())
        else:
            return jsonify({"msg":"the password is incorrect"})
    return jsonify({"msg":"the fields are incorrect"})

@page.route('/logout', methods=['GET'])
def logout():
    if '_user_id' in session:
        user_id = int(session['_user_id'])
        print(user_id)
        logout_user()
        return jsonify({"msg":"the session was closed"})
    return jsonify({"msg":"Not logged in"})