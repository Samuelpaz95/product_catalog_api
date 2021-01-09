from flask import Blueprint
from flask import request
from flask.json import jsonify
from .models import Product, Database, User
from multiprocessing import Value

db = Database()
page = Blueprint('page', __name__)
counter = {}

@page.route('/')
def index():
    return str('<h1>hello, welcome to product catalog<h1>')

@page.route('/users', methods=['GET'])
def users():
    users = db.session.query(User).all()
    list_users = {}
    for user in users:
        list_users[user.user_ID] = {
            'full_name' : user.full_name,
            'username' : user.username,
            'email' : user.email,
        }
    return jsonify(list_users)

@page.route('/add_user', methods=['POST'])
def add_user():
    full_name = request.json['full_name']
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']
    new_user = User(full_name, username, password, email)
    notify = new_user.save(db)
    return jsonify(notify)

@page.route('/users/update/<user_ID>', methods=['PUT'])
def update_user(user_ID):
    db.config_engine(user='catalog_admin', password='adminpassword') # this line will be removed
    if update_element(User, User.user_ID, user_ID, request.json):
        notify = create_notify(user_ID=user_ID, updated_fields=list(request.json.keys()))
    else:
        notify = create_notify(done=False, message='Invalid fields')
    return jsonify(notify)

@page.route('/users/delete/<user_ID>', methods=['DELETE'])
def delete_user(user_ID):
    db.config_engine(user='catalog_admin', password='adminpassword') # this line will be removed
    user = db.session.query(User).get(user_ID)
    db.session.delete(user)
    notify = {
        'done':True,
        'deleted_user_data': {
            'full_name' : user.full_name,
            'username' : user.username,
            'email' : user.email,
        }
    }
    db.session.commit()
    return jsonify(notify)

@page.route('/login', methods=['GET', 'POST'])
def login():
    return "404, page, not found", 404

@page.route('/products', methods=['GET'])
def products():
    products = db.session.query(Product).all()
    list_products = {}
    for i, product in enumerate(products):
        list_products[product.product_ID] = product.to_json()
    return jsonify(list_products)

@page.route('/products/<product_ID>', methods=['GET'])
def products_by_id(product_ID):
    product = db.session.query(Product).get(product_ID)
    if product is not None:
        out = count_product_views(product_ID)
        product_json = product.to_json()
        product_json['views'] = out
        return jsonify(product_json)
    return jsonify({'error':404, 'message':'Resource not found'}), 404

@page.route('/products/update/<product_ID>', methods=['PUT'])
def update_product(product_ID):
    db.config_engine(user='catalog_admin', password='adminpassword') # this line will be removed
    if update_element(Product, Product.product_ID, product_ID, request.json):
        notify = create_notify(product_ID=product_ID, updated_fields=list(request.json.keys()))
    else:
        notify = create_notify(done=False, message='Invalid fields')
    return jsonify(notify)

@page.route('/products/delete/<product_ID>', methods=['DELETE'])
def delete_product(product_ID):
    db.config_engine(user='catalog_admin', password='adminpassword') # this line will be removed
    product = delete_element(Product, product_ID)
    if product is not None:
        notify = create_notify(done=True, message='Product removed successfully', 
                               element_deleted=product.to_json())
        return jsonify(notify)
    else:
        notify = create_notify(done=False, message='404, element not found')
        return jsonify(notify), 404

# utility functions

def update_element(cls, id_field, id:int, data) -> bool:
    db.config_engine(user='catalog_admin', password='adminpassword') # this line will be removed
    product = db.session.query(cls).filter(id_field == id)
    done = not True
    try:
        rows_affected = product.update(data)
        done = rows_affected > 0
        db.session.commit()
    except:
        db.session.rollback()
    return done

def delete_element(cls, id:int):
    element = db.session.query(cls).get(id)
    if element is not None:
        db.session.delete(element)
        db.session.commit()
    return element

def create_notify(done:bool=True, message:str='action completed successfully', **details) -> dict:
    details['done'] = done
    details['message'] = message
    return details

def count_product_views(product_ID):
    if product_ID not in counter:
        counter[product_ID] = Value('i', 0)
    with counter[product_ID].get_lock():
        counter[product_ID].value += 1
        out = counter[product_ID].value
    return out
