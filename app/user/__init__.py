# coding: utf-8
# __author__: ""

from flask import Blueprint
user = Blueprint('user', __name__)
from . import views
