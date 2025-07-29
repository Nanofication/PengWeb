from flask import Blueprint, render_template
from app.models.product import Product

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def render_home():
    featured_items = Product.query.order_by(Product.amount.asc()).limit(8).all()

    #Add nes pics for the slide in the home page
    carousel_images = [
        'images/slide.jpg',
        'images/slide1.jpg',
    ]

    return render_template('index.html',
                           featured_items=featured_items,
                           carousel_images=carousel_images)
