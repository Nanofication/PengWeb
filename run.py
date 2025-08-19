from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app import db

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pengweb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'suppose-to-work'

db.init_app(app)
migrate = Migrate(app, db)

# Register Blueprints
from app.controllers.product_controller import product_bp
from app.controllers.home_controller import home_bp
from app.controllers.contact_controller import contact_bp
from app.controllers.about_controller import about_bp
from app.controllers.footer_controller import footer_bp
from app.controllers.auth_controller import auth_bp

app.register_blueprint(home_bp)
app.register_blueprint(product_bp)
app.register_blueprint(contact_bp)
app.register_blueprint(about_bp)
app.register_blueprint(footer_bp)
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(debug=True)
