# coding: utf-8
# __author__: ""

from app.dept import dept
from utils.logger import logger
from flask import jsonify, abort, Response
import json


dept_data = [
    {
        'name': '部门1',
        'id': 12345
    },
    {
        'name': '部门2',
        'id': 12346
    }
]


@dept.route('/<int:id>', methods=['GET', ])
def get(id):
    for dt in dept_data:
        if int(dt['id']) == id:
            return jsonify(status='success', dept=dt)

    # return jsonify(status='failed', msg='dept not found')
    logger().error("请求的 数据数据为:{0}".format(id))
    logger().info("info === 请求的 数据数据为:{0}".format(id))
    # tt = 1 / 0
    abort(403)


@dept.route('/depts', methods=['GET', ])
def get_depts():
    data = {
        'status': 'success',
        'depts': dept_data
    }

    return json.dumps(data, ensure_ascii=False, indent=1)
