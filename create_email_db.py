from run import app
from app import db
from app.models.email import UserInfo

with app.app_context():
    # Add fresh data
    userInfo = UserInfo(name="", email="")

    db.session.add(userInfo)
    db.session.commit()

    print("Database reset and seeded.")


# with app.app_context():
#
#     #add amount for "top items" filter
#     products = Product.query.all()
#     for p in products:
#         if p.amount is None:
#             p.amount = 100
#     db.session.commit()
#     print("Existing products updated with amount.")
#
#     #add more data
#     example = Product(
#         name="Example3",
#         category="dog",
#         image_url="images/dog1.jpg"
#     )
#
#     db.session.add(example)
#     db.session.commit()
#     print("New product 'example' added.")
    '''
    #delete data
    last_product = Product.query.order_by(Product.id.desc()).first()
    if last_product:
        print(f"Deleting: {last_product.name}")
        db.session.delete(last_product)
        db.session.commit()
        print("Last product deleted.")
    else:
        print("No products found.")
    


    #add img for new data
    #p1 = db.session.get(Product, 5)
    p2 = db.session.get(Product, 6)

    #p1.image_url = 'images/dog4.jpg'
    p2.image_url = 'images/dog.jpg'

    db.session.commit()
    print("Updated example1 and example2 with image URLs.")
    '''

