"""
@author: Jim
@project: lifeAssistant
@file: article.py
@time: 2019/12/31 9:52
@desc:  
"""

from flask import jsonify, request
from flask.blueprints import Blueprint

from lifeAssistant.libs.mongo_flask import MongoEncoder
from lifeAssistant.models.article import Article

bp = Blueprint("article", __name__, url_prefix="/article")
bp.json_encoder = MongoEncoder


@bp.route("/", methods=("GET",))
def article_list():
    query = Article.objects

    # category 条件
    category_filter = request.args.get("category", None)
    if category_filter:
        query = query(category=category_filter)

    # 分页
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 10))
    results = query.paginate(page=page, per_page=per_page)

    return jsonify(results.items)


@bp.route("/<id>/", methods=("GET",))
def article(id: str):
    instance = Article.objects.get_or_404(id=id)

    return jsonify({
        "code": 0,
        "msg": "success",
        "data": instance
    })
