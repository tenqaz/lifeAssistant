"""
@author: Jim
@project: lifeAssistant
@file: article.py
@time: 2019/12/31 9:52
@desc:  
"""

import os
import uuid

import arrow
from flask import jsonify, request, current_app
from flask.blueprints import Blueprint
from flask_restful import Resource, Api
from werkzeug.utils import secure_filename

from lifeAssistant.enums import ArticleTypeEnum
from lifeAssistant.libs.mongo_flask import MongoEncoder
from lifeAssistant.models.article import Article

bp = Blueprint("article", __name__, url_prefix="/article")
bp.json_encoder = MongoEncoder

api = Api(bp)


class ArticleApi(Resource):

    def get(self, id: str):
        instance = Article.objects.only("content").get_or_404(id=id)

        return jsonify({
            "code": 0,
            "msg": "success",
            "data": instance
        })

    def delete(self, id: str):
        instance = Article.objects(id=id).first()
        # 删除图片
        img_url = "{}/{}".format(current_app.config['IMG_PATH'], instance.header_img)
        os.remove(img_url)

        instance.delete()

        return jsonify({
            "code": 0,
            "msg": "success",
            "data": "",
        })


class ArticlesApi(Resource):

    def allowed_file(self, filename: str) -> bool:
        """
            检验扩展名. 判断文件是否上传
        Returns:

        """
        ALLOWED_EXTENSIONS = ["jpg", "png", "gif", "bmp"]

        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def post(self):
        instance = Article()
        instance.category = request.form.get("category", None)
        instance.category2 = request.form.get("category2", None)
        instance.header = request.form.get("header", None)
        instance.content = request.form.get("content", None)
        instance.publisher = request.form.get("publisher", None)
        instance.publisher_time = request.form.get("publisher_time", None)
        instance.create_time = arrow.now().format("YYYY-MM-DD hh-mm-ss")
        instance.type = ArticleTypeEnum.ManualKind.value

        # 文件上传
        img_file = request.files.get("header_img", None)
        print(img_file.filename)
        if img_file and self.allowed_file(img_file.filename):
            filename = secure_filename(img_file.filename)
            img_name = uuid.uuid4().hex

            filename = "{}{}".format(img_name, os.path.splitext(filename)[-1])
            img_file.save("{}/{}".format(current_app.config['IMG_PATH'], filename))
            instance.header_img = filename

        instance.save()
        return jsonify({
            "code": 0,
            "msg": "success",
            "data": instance
        })

    def get(self):
        query = Article.objects.exclude("content")

        # category 条件
        category_filter = request.args.get("category", None)
        if category_filter:
            query = query(category=category_filter)

        # 分页
        page = int(request.args.get("page", 1))
        per_page = int(request.args.get("per_page", 10))
        results = query.paginate(page=page, per_page=per_page)

        return jsonify({
            "code": 0,
            "msg": "success",
            "data": results.items
        })


# @bp.route("/", methods=("GET",))
# def article_list():
#     query = Article.objects.exclude("content")
#
#     # category 条件
#     category_filter = request.args.get("category", None)
#     if category_filter:
#         query = query(category=category_filter)
#
#     # 分页
#     page = int(request.args.get("page", 1))
#     per_page = int(request.args.get("per_page", 10))
#     results = query.paginate(page=page, per_page=per_page)
#
#     return jsonify({
#         "code": 0,
#         "msg": "success",
#         "data": results.items
#     })


# @bp.route("/<id>/", methods=("GET",))
# def article(id: str):
#     instance = Article.objects.only("content").get_or_404(id=id)
#
#     return jsonify({
#         "code": 0,
#         "msg": "success",
#         "data": instance
#     })


api.add_resource(ArticleApi, '/<string:id>')
api.add_resource(ArticlesApi, '/')
