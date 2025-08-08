from app import db

class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255))

    def __repr__(self):
        return f"<Product {self.name}>"

def get_all_users():
    return UserInfo.query.all()

def save_user(name, email):
    userInfo = UserInfo(name=name, email=email)

    db.session.add(userInfo)
    db.session.commit()

def find_email(email):
    return UserInfo.query.filter_by(email=email).first()
