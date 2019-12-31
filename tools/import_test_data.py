"""
@author: Jim
@project: lifeAssistant
@file: import_test_data.py
@time: 2019/12/31 10:42
@desc:

    mongo中插入测试数据
"""

from pymongo import MongoClient

db = MongoClient(host="192.168.0.206", port=27017)

article = db['lifeAssistant']['article']

data = [
    {"category": "前沿", "category2": "", "title": "如何与家里的猫建立牢固的关系？", "publisher": "新浪科技", "publisher_time": "2019-12-30", "create_time": "2019-12-31 13:00:12", "content": "哈哈"},
    {"category": "前沿", "category2": "", "title": "乐享生活 | 你知道2019年的这几个“黑科技”吗？", "publisher": "科普中国-科学原理一点通", "publisher_time": "2019-12-30", "create_time": "2019-12-31 14:00:15", "content": "德玛西亚"},
    {"category": "百科", "category2": "", "title": "“雪球地球”时期的生物是如何存活的？", "publisher": "新浪科技", "publisher_time": "2019-12-30", "create_time": "2019-12-31 17:21:12", "content": "你的剑就是我的剑"},
    {"category": "军事", "category2": "", "title": "为什么世界上可见的高超声速飞行器都是扁平的？", "publisher": "科普中国-军事科技前沿", "publisher_time": "2019-12-30", "create_time": "2019-12-31 14:00:15", "content": "我也不知道"},
]
article.insert_many(data)
