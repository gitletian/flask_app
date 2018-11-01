# coding: utf-8
# __author__: ""
from flask import Flask
from flask_login import LoginManager
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel

# 加载 db
db = SQLAlchemy()

# 加载 login 插件
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

# 加载国际化
babel = Babel()


def create_app(config_name="default"):
    app = Flask(__name__, static_folder='../static', template_folder='../templates')

    # 初始化配置
    app.config.from_object(config[config_name])  # 加载配置文件
    config[config_name].init_app(app)  # 调用配置信息的初始化环境的静态方法

    # 注册其他组件
    # 初始化数据 model 组件
    db.init_app(app)
    login_manager.init_app(app)
    babel.init_app(app)

    # 注册蓝图, 必须放在 create_app 中导入, 否在 在 user中无法识别 db
    from .user import user as user_blueprint
    from .voice import voice as voice_blueprint
    from .brother import brother as brother_blueprint

    app.register_blueprint(user_blueprint, url_prefix='/user')
    app.register_blueprint(voice_blueprint)
    app.register_blueprint(brother_blueprint)

    return app

