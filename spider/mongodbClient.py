"""
@author: Jim
@project: lifeAssistant
@file: mongodbClient.py
@time: 2019/12/27 10:28
@desc:

    mongodb的工具类
"""

import pymongo

from typing import Callable, TypeVar, Any, List, Dict
import functools
import time

MongoDictType = Dict[str, Any]
T = TypeVar('T')


def operation_wraps(func: Callable[..., T]) -> T:
    @functools.wraps(func)
    def wraps(self, *args: Any, **kwargs: Any) -> T:

        # 重试次数
        retry_num = 5

        while retry_num:

            if self.is_conn():
                return func(self, *args, **kwargs)
            else:
                self.conn()
                time.sleep(0.1)

            retry_num -= 1

        raise Exception("mongodb 连接失败..")

    return wraps


class MongodbClient:

    def __init__(self, database: str, url: str = "localhost:27017"):
        """

        Args:
            url: mongdb的url
            database: 选择的数据库
        """
        self._url: str = url
        self._database: str = database
        self.client: pymongo.MongoClient = None
        self.db: pymongo.database.Database = None
        self.collection: pymongo.collection.Collection = None  # 集合

        self.conn()

    def conn(self) -> None:
        """
            连接mongodb，并选择使用的数据库.
        Returns:

        """
        self.client = pymongo.MongoClient(self._url)
        self.db = self.client[self._database]

    def select(self, collection: str) -> None:
        """
            选择使用的集合
        Args:
            collection: 集合

        Returns:

        """
        self.collection = self.db[collection]

    def is_conn(self) -> bool:
        if self.db and self.client:
            return True
        else:
            return False

    @operation_wraps
    def insert_one(self, data: MongoDictType) -> pymongo.results.InsertOneResult:
        """
            插入一条数据

        Args:
            collection: 集合
            data: 插入的数据

        Returns:
            返回插入的结果

        """
        ret = self.collection.insert_one(data)
        return ret

    @operation_wraps
    def insert_many(self, data: List[MongoDictType]) -> pymongo.results.InsertOneResult:
        """
            插入多条数据

        Args:
            collection: 集合
            data: 插入的数据

        Returns:

        """
        ret = self.collection.insert_many(data)
        return ret

    @operation_wraps
    def find(self, condition: MongoDictType, columns: List[str]):
        """

        Args:
            collection: 文档
            condition:
            columns:

        Returns:

        """

        return self.collection.find(condition, columns)

    @operation_wraps
    def close(self):
        """
            关闭mongo连接

        Returns:

        """
        self.client.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


if __name__ == '__main__':
    client = MongodbClient("127.0.0.1:27017", "test")
    client.select("student")
    client.insert_one({"name": "zhangsan", "age": 18})
    client.insert_many([{"name": "lisi", "age": 99}, {"name": "wangwu", "age": 88}])
    client.close()

    # with MongodbClient("192.168.0.206:27017", "test") as client:
    #     client.insert_one("student", {"name": "zheng", "age": 77, "sex": "male"})
