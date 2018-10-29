# coding: utf-8
# __author__: ""
import os
from logging import INFO, ERROR
from utils.logger import RotatingFileHandlerUser


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SSL_DISABLE = False
    SQLALCHEMY_RECORD_QUERIES = True

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
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://xxx:xxx@127.0.0.1/xxx?charset=utf8'

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
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://xxx:xxx@127.0.0.1/xxx?charset=utf8'

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
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://xxx:xxx@127.0.0.1/xxx?charset=utf8'

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
