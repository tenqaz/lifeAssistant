"""
@author: Jim
@project: lifeAssistant
@file: kepuchinaSpider.py
@time: 2019/12/26 15:16
@desc:

    爬取科普中国的数据
"""

import requests
from bs4 import BeautifulSoup

from typing import List, Dict, Any
import arrow
from spider.mongodbClient import MongodbClient
from lifeAssistant.config import IMG_PATH, MONGODB_SETTINGS
from lifeAssistant.enums import ArticleTypeEnum
import os

import uuid

index_url = "https://www.kepuchina.cn"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"
                  " AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/70.0.3538.77 Safari/537.36",
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
}


def get_category() -> Dict:
    """
        获取导航栏的链接
    Returns:

    """
    rsp = requests.get(index_url, headers=headers)
    rsp.encoding = 'utf8'
    if rsp.status_code == 200:
        text = rsp.text

        # 解析导航栏，获取 标题:url
        category_dict = dict()
        soup = BeautifulSoup(text, 'lxml')
        category_list = soup.select("body > div.header > div.header_in > div.menu > ul > li")
        for category in category_list[:-1]:
            category_dict[category.a.string] = category.a['href']

        return category_dict
    else:
        raise Exception("获取列表失败")


def get_page_url(category_url: Dict):
    """
        获取文章的url
    Args:
        category_url: {category: url}

    Returns:
        一级分类名, 文章url，图片名称.

    """

    for category, url in category_url.items():
        if "http" not in url:
            url = index_url + url

        rsp = requests.get(url, headers=headers)
        if rsp.status_code == 200:
            text = rsp.text

            soup = BeautifulSoup(text, "lxml")
            page_list = soup.select(
                "body > div > div.content > div.layout-right-cont > div > div.layoutLeft > div > div")
            for page in page_list:
                # 保存图片
                img_url = url + page.a.img.get("src", None)
                resp_img = requests.get(img_url, headers=headers)
                img = resp_img.content

                suffix = os.path.splitext(img_url)[1]
                img_id = uuid.uuid4().hex
                img_name = "{}{}".format(img_id, suffix)
                header_img = "{}/{}".format(IMG_PATH, img_name)
                with open(header_img, "wb") as f:
                    f.write(img)

                yield (category, url + page.a['href'][1:], img_name)


def get_page_content(url: str) -> Dict[str, str]:
    """
        获取详细页的数据
    Args:
        url:

    Returns:

    """

    data = {}

    rsp = requests.get(url, headers=headers)
    rsp.encoding = "utf8"
    if rsp.status_code == 200:
        text = rsp.text
        # with open("tmp.txt", "w", encoding="utf8e") as f:
        #     f.write(text)
        soup = BeautifulSoup(text, "lxml")
        data['header'] = soup.select(
            "body > div.content_main > div.content_left > div.heading > div > table > tr > td:nth-child(2) > h1")[
            0].string
        data['publisher'] = soup.select(
            "body > div.content_main > div.content_left > div.heading > div > table > tr > td:nth-child(2) > p > span:nth-child(1)")[
            0].string
        data['publisher_time'] = soup.select(
            "body > div.content_main > div.content_left > div.heading > div > table > tr > td:nth-child(2) > p > span:nth-child(2)")[
            0].string
        content_tag = soup.select("body > div.content_main > div.content_left > div.content_detail > div")[0]
        content = ""
        for p_tag in content_tag:
            if p_tag.string:
                content += p_tag.string.strip() + "\n"

        data['content'] = content

    return data


if __name__ == '__main__':
    category_url: Dict = get_category()

    page_urls = get_page_url(category_url)

    for category, url, header_img in page_urls:
        # url = "https://www.kepuchina.cn/tech/info/201912/t20191227_1178163.shtml"
        rst = get_page_content(url)
        rst['category'] = category
        rst['header_img'] = header_img
        rst['create_time'] = arrow.now().format("YYYY-MM-DD HH:mm:ss")
        rst['type'] = ArticleTypeEnum.SpiderKind.value
        with MongodbClient(MONGODB_SETTINGS['db'],
                           "{}:{}".format(MONGODB_SETTINGS['host'], MONGODB_SETTINGS['port'])) as client:
            client.select("article")
            client.insert_one(rst)
