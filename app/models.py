# coding: utf-8
# __author__: ""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # db是在app/__init__.py生成的关联后的SQLAlchemy实例


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    email = db.Column(db.String(320), unique=True)
    password = db.Column(db.String(32), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    '''
    db.relationship()的第一个参数表明这个关系的另一端是那个模型。
    backref: 参数向User模型中添加一个role模型, 从而定义反向关系。
    这一属性可替代 role_id 访问Role模型，此时获取的是模型对象，而不是外键的值。
    db.relationship()表示多对一关系时，把 uselist 设置为False,把多变成一
    加入了lazy=’dynamic’参数，从而禁止自动执行查询
    user_role.users会返回一个尚未执行的查询，因此可以在其上添加过滤器
    '''
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class Dept(db.Model):
    __tablename__ = 'dept'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    desc = db.Column(db.String(320), unique=True)

    def __repr__(self):
        return '<Dept %r>' % self.username




