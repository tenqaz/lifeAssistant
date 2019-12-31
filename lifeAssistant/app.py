"""
@author: Jim
@project: lifeAssistant
@file: app.py
@time: 2019/12/31 9:50
@desc:  
"""

from flask import Flask
from extension import mongodb
from api.article import bp


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
    app.register_blueprint(bp)


def create_app():
    app = Flask(__name__)

    app.config.from_object("config")

    register_plugin(app)
    register_blueprint(app)

    return app


if __name__ == '__main__':
    app = create_app()

    app.run()
