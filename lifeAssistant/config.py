"""
@author: Jim
@project: lifeAssistant
@file: config.py
@time: 2019/12/31 10:09
@desc:  
"""

from lifeAssistant.libs.mongo_flask import MongoEncoder

import os

# 根据当前环境选择配置
FLASK_ENV = os.getenv("FLASK_ENV")
if FLASK_ENV == 'development':
    MONGODB_SETTINGS = {
        "db": "lifeAssistant",
        "host": "127.0.0.1",
        "port": 27017
    }
else:
    MONGODB_SETTINGS = {
        "db": "lifeAssistant",
        "host": "127.0.0.1",
        "port": 27017
    }

JSON_AS_ASCII = False
