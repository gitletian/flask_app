# coding: utf-8
# __author__: ""

from . import error
from app.utils.logger import logger


@error.app_errorhandler(404)
def page_not_found(e):
    logger().info("============test 404===========")
    return 'bad request...!', 400


@error.app_errorhandler(403)
def page_forbidden(ex):
    return 'forbidden!', 403


@error.app_errorhandler(500)
def internal_server_error(ex):
    return 'server error!'

