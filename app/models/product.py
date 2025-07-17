from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(255))
    price = db.Column(db.Float, nullable=False)
    min_order_qty = db.Column(db.Integer, nullable=False)
    details = db.Column(db.String(200))

    def __repr__(self):
        return f"<Product {self.name}>"

def get_all_products():
    return Product.query.all()
