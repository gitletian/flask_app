# coding: utf-8
# __author__: ""
from flask import Flask
from config import config

from error import error
from app.dept import dept
from app.user import user

from app.models import db


def create_app(config_name="default"):
    app = Flask(__name__)

    # 初始化配置
    app.config.from_object(config[config_name])  # 加载配置文件
    config[config_name].init_app(app)  # 调用配置信息的初始化环境的静态方法

    # 注册蓝图
    app.register_blueprint(error, url_prefix='/error')
    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(dept, url_prefix='/dept')

    # 注册其他组件
    # 初始化数据 model 组件
    db.init_app(app)

    return app

