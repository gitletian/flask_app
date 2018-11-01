# coding: utf-8
# __author__: ""

from flask import Blueprint
voice = Blueprint('voice', __name__)
from . import views
