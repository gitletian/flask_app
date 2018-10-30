# coding: utf-8
# __author__: ""
import logging
from logging.handlers import RotatingFileHandler
from flask import current_app


class InfoFilter(logging.Filter):
    def filter(self, record):
        """
        only use INFO  and WARNING
        筛选, 只需要 INFO and WARNING 级别的log
        :param record:
        :return:
        """
        if logging.INFO <= record.levelno < logging.ERROR:
            # 如果 是 INFO 或 WARNING 返回 ture
            return super().filter(record)
        else:
            return False


class RotatingFileHandlerUser(RotatingFileHandler):
    fmt = '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'

    def __init__(self, level, filename):
        RotatingFileHandler.__init__(self, filename=filename)
        self.level = level
        self.formatter = logging.Formatter(fmt=self.fmt)


# 初始化日志组件
def logger():
    return current_app.logger

