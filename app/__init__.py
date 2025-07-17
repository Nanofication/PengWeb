from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Load .env at startup
load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Read DB config from environment
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_NAME = os.getenv('DB_NAME')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '3306')
    SECRET_KEY = os.getenv('SECRET_KEY')

    # Set SQLAlchemy URI
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = SECRET_KEY

    db.init_app(app)

    # Register blueprints
    from app.controllers.product_controller import product_bp
    from app.controllers.home_controller import home_bp
    from app.controllers.contact_controller import contact_bp
    app.register_blueprint(product_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(contact_bp)

    return app



