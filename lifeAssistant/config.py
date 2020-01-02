"""
@author: Jim
@project: lifeAssistant
@file: config.py
@time: 2019/12/31 10:09
@desc:  
"""

from lifeAssistant.libs.mongo_flask import MongoEncoder

MONGODB_SETTINGS = {
    "db": "lifeAssistant",
    "host": "192.168.0.206",
    "port": 27017
}

JSON_AS_ASCII = False
