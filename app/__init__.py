from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@127.0.0.1:3306/test"

app.config['SQLALCHEMY_ECHO'] = True  # True为打印每条sql记录

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  #

db = SQLAlchemy(app)


class TUser(db.Model):
    """
    用户表
    """
    __tabalename__ = 't_user_2'
    id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(64), unique=True)
    phone = db.Column(db.Integer, default=123456)
    phone_status = db.Column(db.Integer, default=0)
    user_status = db.Column(db.Integer, default=0)
    user_password = db.Column(db.Integer, default=0)
    create_time = db.Column(db.DateTime, default=0)
    update_time = db.Column(db.DateTime, default=0)

    def __init__(self, uid, password, name):
        self.uid = uid
        self.password = password
        self.name = name


class TCurrency(db.Model):
    """
    币种表
    """
    __tablename__ = "t_currency"
    currency_id = db.Column(db.Integer, primary_key=True, unique=True)
    currency_name = db.Column(db.String(128),)
    currency_status = db.Column(db.Integer, default=0)
    currency_create_time = db.Column(db.DateTime, default=0)
    currency_contract_address = db.Column(db.String(512))
    currency_update_time = db.Column(db.DateTime, default=0)
    currency_withdraw_commission = db.Column(db.Float, default=0)
    currency_extract_count_min = db.Column(db.Float)

class TUserBalance(db.Model):
    """
    合约列表
    """
    __tabalename__ = "t_user_balance"
    balance_id = db.Column(db.String(128), primary_key=True, unique=True, index=True )
    sa_user_id = db.Column(db.String(128), db.ForeignKey("t_user.id"))


if __name__ == '__main__':
    db.create_all()
    user_1 = TUser(uid="1", password="123", name="jack")
    db.session.add(user_1)
    db.session.commit()