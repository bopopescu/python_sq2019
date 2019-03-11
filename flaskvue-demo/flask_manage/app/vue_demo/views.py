# -*- coding: utf-8 -*-

# @Time    : 2018/12/6 16:30
# @Author  : songq001
# @Comment : 


from . import vue_demo
from flask import render_template, jsonify
from random import *
import requests
from flask_cors import CORS


# 解决跨域问题
CORS(vue_demo)

@vue_demo.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)


@vue_demo.route('/', defaults={'path': ''})
@vue_demo.route('/<path:path>')
def catch_all(path):
    if path:
        print(path)
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")





