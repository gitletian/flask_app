# coding: utf-8
# __author__ = "john.pan"

from app.models import db
from sqlalchemy.sql import text
from flask import current_app
from redis import Redis
import threading


class DB:
    def __init__(self, name=None):
        self.conn = db.get_engine(bind=name).connect()

    def query(self, sql, meta=False):
        result = self.conn.execute(text(sql))

        columns = [_.lower() for _ in result.keys()]
        results = [dict(zip(columns, row)) for row in result]

        if meta:
            return results, columns

        return results

    def __del__(self):
        self.conn.close()


class MpRedis(Redis):
    '''
    配置 redis
    db:
        1 接口 黑白名单使用
        2 授权信息
        3 登陆
    '''
    redis = [None] * 12
    _instance_lock = threading.Lock()

    # redis_conf = dict(host=settings.REDIS_IP, port=settings.REDIS_PORT)
    # redis_conf = current_app.config["REDIS_CONF"]

    def __init__(self, db, *args, **kwargs):
        pass

    def __new__(cls, db, *args, **kwargs):
        redis_conf = current_app.config["REDIS_CONF"]
        if not cls.redis[db]:
            # 支持多线程
            with cls._instance_lock:
                if not cls.redis[db]:
                    o = Redis.__new__(cls, *args)
                    # Redis.__init__(o, db=db, **cls.redis_conf)
                    Redis.__init__(o, db=db, **redis_conf)
                    cls.redis.insert(db, o)

        return cls.redis[db]


