# coding: utf-8
# __author__: ""

from flask import Blueprint

# 初始化蓝图
dept = Blueprint('dept', __name__,)

from app.dept import views