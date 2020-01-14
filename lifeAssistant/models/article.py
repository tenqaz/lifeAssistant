"""
@author: Jim
@project: lifeAssistant
@file: article.py
@time: 2019/12/30 16:43
@desc:
    文章的model类
"""
from lifeAssistant.extension import mongodb



class Article(mongodb.Document):
    category = mongodb.StringField()
    category2 = mongodb.StringField()
    header = mongodb.StringField()
    content = mongodb.StringField()
    publisher = mongodb.StringField()
    publisher_time = mongodb.StringField()
    header_img = mongodb.StringField()  # 封面图片. 名称
    type = mongodb.IntField()  # 存储方式. 0：爬虫存储. 1: 手动上传存储
    click_num = mongodb.IntField()  # 点击次数
    create_time = mongodb.StringField()
