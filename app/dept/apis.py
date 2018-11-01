# coding: utf-8
# __author__: ""
from app.utils.db import DB


def all_dept():
    '''
    之行sql 获取所有 dept
    :return:
    '''
    dept = DB().query("select * from users")
    # dept = []
    return dept
