# coding: utf-8
# __author__: ""
import os
from logging import INFO, ERROR
from utils.logger import RotatingFileHandlerUser


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SSL_DISABLE = False

    #  可以用于显式地禁用或者启用查询记录。查询记录 在调试或者测试模式下自动启用
    SQLALCHEMY_RECORD_QUERIES = True
    # 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # redis 配置参数
    REDIS_CONF = dict(host='172.16.1.100', port=6379)

    # 日志配置参数
    LOG_PATH = os.path.join(basedir, 'logs')
    os.path.exists(LOG_PATH) or os.mkdir(LOG_PATH)

    LOG_PATH_ERROR = os.path.join(LOG_PATH, 'error.log')
    LOG_PATH_INFO = os.path.join(LOG_PATH, 'info.log')
    LOG_FILE_MAX_BYTES = 100 * 1024 * 1024
    # 轮转数量是 10 个
    LOG_FILE_BACKUP_COUNT = 10

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    DEBUG = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False

    # 每次请求结束都会自动提交事务
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 配置数据库引擎
    # eg: dialect+driver://username:password@host:port/database
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flask_app:123456@172.16.1.100/flask_app?charset=utf8'
    # 创建多个数据库引擎, 如果没指定, 会用默认 的 SQLALCHEMY_DATABASE_URI
    # SQLALCHEMY_BINDS = {
    #     'mysql': 'mysql+pymysql://flask_app:123456@172.16.1.100/flask_app?charset=utf8',
    #     'sqllite': 'sqlite:////path/to/appmeta.db',
    #     'pg': 'postgresql://flask_app:123456@172.16.1.100:5432/flask_app',
    # }

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        # FileHandler Info
        file_handler_info = RotatingFileHandlerUser(INFO, cls.LOG_PATH_INFO)
        # file_handler_info.addFilter(InfoFilter())
        app.logger.addHandler(file_handler_info)

        # FileHandler Error
        file_handler_error = RotatingFileHandlerUser(ERROR, cls.LOG_PATH_ERROR)
        app.logger.addHandler(file_handler_error)

        # streaming handler


class AutConfig(Config):
    DEBUG = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flask_app:123456@172.16.1.100/flask_app?charset=utf8'

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        # FileHandler Info
        file_handler_info = RotatingFileHandlerUser(INFO, cls.LOG_PATH_INFO)
        # file_handler_info.addFilter(InfoFilter())
        app.logger.addHandler(file_handler_info)

        # FileHandler Error
        file_handler_error = RotatingFileHandlerUser(ERROR, cls.LOG_PATH_ERROR)
        app.logger.addHandler(file_handler_error)


class ProConfig(Config):
    DEBUG = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flask_app:123456@172.16.1.100/flask_app?charset=utf8'

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        # FileHandler Info
        file_handler_info = RotatingFileHandlerUser(INFO, cls.LOG_PATH_INFO)
        # file_handler_info.addFilter(InfoFilter())
        app.logger.addHandler(file_handler_info)

        # FileHandler Error
        file_handler_error = RotatingFileHandlerUser(ERROR, cls.LOG_PATH_ERROR)
        app.logger.addHandler(file_handler_error)


config = {
    'default': DevConfig,
    'dev': DevConfig,
    'aut': AutConfig,
    'pro': ProConfig,
}
