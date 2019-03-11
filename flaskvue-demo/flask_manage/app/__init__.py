# -*- coding: utf-8 -*-

# @Time    : 2018/12/4 10:54
# @Author  : songq001
# @Comment : 


from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager
from flask_cors import CORS
import requests
from random import *


db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'show.login'


def create_app(config_name):
    """ 使用工厂函数初始化程序实例"""
    app = Flask(__name__, template_folder="templates")

    app.config.from_object(config[config_name])
    config[config_name].init_app(app=app)

    db.init_app(app=app)
    login_manager.init_app(app=app)

    @app.route('/', methods=['GET', ])
    def index():
        return "Hello Flask!"

    # 注册蓝本 show
    from .show import show as show_blueprint
    app.register_blueprint(show_blueprint, url_prefix='/show')

    return app


def create_app02(config_name):
    """ 使用工厂函数初始化程序实例"""
    app = Flask(__name__, static_folder="../../dist/static", template_folder="../../dist")
    app.config.from_object(config[config_name])
    config[config_name].init_app(app=app)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})       # 解决跨域问题

    db.init_app(app=app)
    db.app = app

    # @app.route('/')
    # def index():
    #     return "Hello Flask!"

    @app.route('/api/random')
    def random_number():
        response = {
            'randomNumber': randint(1, 100)
        }
        return jsonify(response)

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def catch_all(path):
        if app.debug:
            return requests.get('http://localhost:8080/{}'.format(path)).text
        return render_template("index.html")
    return app

