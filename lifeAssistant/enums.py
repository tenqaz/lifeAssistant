"""
@author: Jim
@project: lifeAssistant
@file: enums.py
@time: 2020/1/14 11:56
@desc:
    枚举
"""

from enum import IntEnum, unique


@unique
class ArticleTypeEnum(IntEnum):
    """
        文章的存储方式.
    """

    SpiderKind = 0  # 爬虫存储
    ManualKind = 1  # 手动存储
