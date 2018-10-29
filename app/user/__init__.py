# coding: utf-8
# __author__: ""

from flask import Blueprint

# 初始化蓝图
user = Blueprint('user', __name__,)

from app.user import views
