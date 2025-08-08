from app import db

class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255))

    def __repr__(self):
        return f"<Product {self.name}>"

def get_all_users():
    return UserInfo.query.all()

def save_user():
    userInfo = UserInfo(name="", email="")

    db.session.add(userInfo)
    db.session.commit()
