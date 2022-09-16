import json
from flask import request, jsonify, Blueprint
from . import db
from .models import Products
from sqlalchemy.sql import func
from sqlalchemy import desc

views = Blueprint('views', __name__)

# db.create_all()

@views.route('/')
def index():
    return 'Hello World!'

@views.route('/products/')
def getProducts():
    products = Products.query.all()

    return jsonify([
        {
            'id': product.id,
            'productName': product.productName,
            'image': product.image,
            'price': product.price,
            'unit': product.unit,
            'sale': product.sale,
            'created_at': product.created_at,
            'updated_at': product.updated_at,
        }
        for product in products
    ])