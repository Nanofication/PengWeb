from run import app
from app import db
from app.models.product import Product

with app.app_context():
    db.drop_all()
    db.create_all()

    # Add fresh data
    p1 = Product(name="Bone Toy", category="dog", image_url="images/testimg1.jpg")
    p2 = Product(name="Catnip Mouse", category="cat", image_url="images/testimg3.jpg")
    p3 = Product(name="Whatever", category="dog", image_url="images/testimg2.jpg")

    db.session.add_all([p1, p2, p3])
    db.session.commit()

    print("Database reset and seeded.")
