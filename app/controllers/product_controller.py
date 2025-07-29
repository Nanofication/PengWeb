from flask import Blueprint, render_template, request, redirect, flash
from app.models.product import Product, get_products_by_category
from app import db

product_bp = Blueprint('product', __name__)

@product_bp.route('/products')
def display_products_page():
    animal = request.args.get('animal')  # "dog" / "cat" / etc.
    page = request.args.get('page', 1, type=int)
    per_page = 20

    query = Product.query
    if animal:
        query = query.filter(Product.category == animal)

    paginated_products = query.paginate(page=page, per_page=per_page)

    return render_template('products.html', products=paginated_products, animal=animal)


