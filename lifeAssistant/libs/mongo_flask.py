"""
@author: Jim
@project: lifeAssistant
@file: mongo_flask.py
@time: 2019/12/31 17:58
@desc:

    使用mongo的工具方法
"""

from json import JSONEncoder
from datetime import datetime, date
from mongoengine.base import BaseDocument
from bson import ObjectId


class MongoEncoder(JSONEncoder):
    def default(self, o):

        # 转换日期
        if isinstance(o, (datetime, date)):
            pass

        # 转换Document
        if isinstance(o, BaseDocument):
            return o.to_mongo()

        # 转换id
        if isinstance(o, ObjectId):
            return str(o)

        return JSONEncoder.default(self, o)
