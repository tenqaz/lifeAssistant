"""
@author: Jim
@project: lifeAssistant
@file: __init__.py
@time: 2020/1/2 15:45
@desc:  
"""

from flask import Flask
from lifeAssistant.extension import mongodb
from lifeAssistant.api.article import bp as article_bp


def register_plugin(app):
    """
        注册插件.
    Args:
        app:

    Returns:

    """

    # 初始化mongodb
    mongodb.init_app(app)


def register_blueprint(app):
    """
        注册蓝图.
    Args:
        app:

    Returns:

    """
    app.register_blueprint(article_bp)


def create_app():
    app = Flask("lifeAssistant")

    app.config.from_object("lifeAssistant.config")

    register_plugin(app)
    register_blueprint(app)

    return app


if __name__ == '__main__':
    app = create_app()

    app.run()
