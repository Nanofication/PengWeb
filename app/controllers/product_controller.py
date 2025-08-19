from flask import Blueprint, render_template, request, redirect, flash, session, url_for, abort
from app.models.product import Product, get_products_by_category
from app import db
from sqlalchemy import select

product_bp = Blueprint('product', __name__)

def admin_required():
    if session.get('role') != 'admin':
        abort(403)

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

@product_bp.route('/products/new', methods=['GET', 'POST'])
def create_product():
    admin_required()
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        image_url = request.form.get('image_url', '').strip()
        category = request.form.get('category', '').strip().lower()
        amount = request.form.get('amount', 0, type=int)
        if not name:
            flash('Product name is required', 'warning')
            return redirect(request.url)
        p = Product(name=name, image_url=image_url, category=category, amount=amount)
        db.session.add(p)
        db.session.commit()
        flash('Product created', 'success')
        return redirect(url_for('product.display_products_page', animal=category or None))
    return render_template('admin_product_form.html', mode='create')

@product_bp.route('/products/<int:pid>/delete', methods=['POST'])
def delete_product(pid):
    admin_required()
    p = Product.query.get_or_404(pid)
    db.session.delete(p)
    db.session.commit()
    flash('Product deleted', 'info')
    return redirect(request.referrer or url_for('product.display_products_page'))
