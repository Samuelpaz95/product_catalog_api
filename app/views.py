from flask import Blueprint
from flask.json import jsonify
from .models import Product, Database

db = Database()
page = Blueprint('page', __name__)

@page.route('/')
def index():
    return str('hello, welcome to product catalog')

@page.route('/login', methods=['GET', 'POST'])
def login():
    pass

@page.route('/list_products', methods=['GET'])
def list_products():
    products = db.session.query(Product).all()
    print(products)
    list_products = {}
    for product in products:
        list_products[product.porduct_ID] = {
            'sku':product.sku,
            'product_name':product.product_name,
            'product_price':product.product_price,
            'brand':product.brand
        }
    return jsonify(list_products)

    