from flask import Blueprint, render_template, request, redirect, flash
from app.models.product import Product, get_products_by_category
from app import db

product_bp = Blueprint('product', __name__)

@product_bp.route('/products')
def display_products_page():
    animal = request.args.get('animal')  # "dog" or "cat"
    products = get_products_by_category(animal)
    return render_template('products.html', products=products)

