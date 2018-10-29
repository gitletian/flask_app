# coding: utf-8
# __author__: ""


from app.user import user
from utils.logger import logger
from flask import jsonify, abort
import json


user_data = [
    {
        'id': 1,
        'name': '张三',
        'age': 23
    },
    {
        'id': 2,
        'name': '李四',
        'age': 24
    }
]


@user.route('/<int:id>', methods=['GET', ])
def get(id):
    for user in user_data:
        if user['id'] == id:
            return jsonify(status='success', user=user)

    logger().info("测试 500")
    abort(500)


@user.route('/users', methods=['GET', ])
def users():
    data = {
        'status': 'success',
        'users': user_data
    }
    return json.dumps(data, ensure_ascii=False, indent=1)
