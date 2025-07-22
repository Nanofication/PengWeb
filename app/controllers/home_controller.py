from flask import Blueprint, render_template
from app.models.product import Product

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def render_home():
    featured_items = Product.query.limit(3).all()  # top 3 products

    carousel_images = [
        'images/slide1.jpg',
        'images/testimg2.jpg',
        'images/slide3.jpg',
    ]

    return render_template('index.html',
                           featured_items=featured_items,
                           carousel_images=carousel_images)
