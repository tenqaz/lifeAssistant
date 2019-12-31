"""
@author: Jim
@project: lifeAssistant
@file: article.py
@time: 2019/12/30 16:43
@desc:
    文章的model类
"""

from extension import mongodb


class Article(mongodb.Document):
    category = mongodb.StringField()
    category2 = mongodb.StringField()
    title = mongodb.StringField()
    content = mongodb.StringField()
    publisher = mongodb.StringField()
    publisher_time = mongodb.StringField()
    create_time = mongodb.StringField()