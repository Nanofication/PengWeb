from flask import Blueprint, render_template, request, redirect, flash
from app.models.product import Product
from app import db

product_bp = Blueprint('product', __name__)

@product_bp.route('/products', methods=['GET', 'POST'])
def products():
    if request.method == 'POST':
        # 获取表单字段
        name = request.form['name']
        image_url = request.form['image_url']
        price = float(request.form['price'])
        min_order_qty = int(request.form['min_order_qty'])
        #details = request.form['details']

        # create&add new product
        new_product = Product(
            name=name,
            image_url=image_url,
            price=price,
            min_order_qty=min_order_qty,
            #details=details
        )
        db.session.add(new_product)
        db.session.commit()
        flash('Product added successfully!')
        return redirect('/products')

    # GET
    products = Product.query.all()
    return render_template('products.html', products=products)

@product_bp.route('/products/delete/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash(f'Product "{product.name}" deleted successfully!')
    return redirect('/products')
