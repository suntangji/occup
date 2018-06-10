# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from main import app


db = SQLAlchemy(app)


class Table(db.Model):
    # 表名
    __tablename__ = 'tables'
    # 桌子id 整形 主键
    table_id = db.Column(db.Integer, primary_key=True)
    floor = db.Column(db.Integer)
    # name = db.Column(db.String(64), unique=True)

    def __init__(self, table_id, floor):
        self.table_id = table_id
        self.floor = floor

    def __repr__(self):
        return '<Table %r>' % self.table_id


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    # 学号 整形 主键
    user_id = db.Column(db.BigInteger, primary_key=True)
    passwd = db.Column(db.String(128))
    # username = db.Column(db.String(64), unique=True, index=True)

    def __init__(self, user_id,password):
        self.user_id = user_id
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.user_id

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.passwd = generate_password_hash(password)

    def confirm_password(self, password):
        return check_password_hash(self.passwd, password)

    def get_id(self):
        return (self.user_id)


class Own(db.Model):
    # 表示桌子被谁占用了
    __tablename__ = 'own'
    table_id = db.Column(db.Integer, db.ForeignKey('tables.table_id'), primary_key=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey('users.user_id'), unique=True)
    leave_time = db.Column(db.Float)
    time = db.Column(db.DateTime)

    def __init__(self, table_id, user_id, leave_time=0):
        import datetime
        self.table_id = table_id
        self.user_id = user_id
        self.leave_time = leave_time    # 离开时长
        self.time = Own.get_time()      # 操作时刻

    @staticmethod
    def get_time():
        import time
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    def __repr__(self):
        return '<Own %r>' % self.table_id


class Suggest(db.Model):
    # 表示桌子被谁占用了
    __tablename__ = 'suggest'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey('users.user_id'))
    context = db.Column(db.Text)
    contact = db.Column(db.Text)
    def __init__(self, user_id, context, contact):
        self.user_id = user_id
        self.context = context
        self.contact = contact

    def __repr__(self):
        return '<Suggest %r>' % self.user_id


class Admin(UserMixin, db.Model):
    __tablename__ = 'admin'
    user_id = db.Column(db.BigInteger, primary_key=True)
    passwd = db.Column(db.String(128))
    # username = db.Column(db.String(64), unique=True, index=True)

    def __init__(self, user_id,password):
        self.user_id = user_id
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.user_id

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.passwd = generate_password_hash(password)

    def confirm_password(self, password):
        return check_password_hash(self.passwd, password)

    def get_id(self):
        return (self.user_id)


class Notice(db.Model):
    # 公告
    __tablename__ = 'notice'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey('admin.user_id'))
    title = db.Column(db.Text)
    context = db.Column(db.Text)
    date = db.Column(db.DateTime)

    def __init__(self, title, context, user_id=1000):
        self.user_id = user_id
        self.title = title
        self.context = context
        self.date = Own.get_time()

    def __repr__(self):
        return '<Notice %r>' % self.title


