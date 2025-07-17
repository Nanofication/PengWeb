from flask import Blueprint, render_template, request, redirect, flash
from app.models.product import Product
from app import db

product_bp = Blueprint('product', __name__)

@product_bp.route('/products', methods=['GET'])
def display_product_page():
    products = Product.query.all()
    return render_template('products.html', products=products)

