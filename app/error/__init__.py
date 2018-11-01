# coding: utf-8
# __author__: ""

from flask import Blueprint

error = Blueprint("error", __name__)

from . import views