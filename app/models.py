from app import db



class TestModels(db.Model):

    __tabalename__ = 't_user_2'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    phone = db.Column(db.Integer, default=123456)
    phone_status = db.Column(db.Integer, default=0)


