# -*- coding: utf-8 -*-

# @Time    : 2018/12/6 16:30
# @Author  : songq001
# @Comment : 
"""
查当前版本号buildNo等：
https://msp-di1.dev.cmrh.com/RH_MSPSERVER/newWechat/apply/getAppVersionConfig?buildNo=286&type=ios&version=1.0.10
查msp-web配置：
https://msp-di1.dev.cmrh.com/dcs/msp-web
"""

from . import msp_interface
from flask import render_template, jsonify
from random import *
import requests
from flask_cors import CORS
from config import Config

base_url = Config.mps_baseUrl
uri = Config.mps_uri

# 解决跨域问题
CORS(msp_interface)

@msp_interface.route('/home')
def random_number():
    return "welcome msp_home page"


# @msp_interface.route('/', defaults={'path': ''}, methods=["POST", "GET"])
# @msp_interface.route('/<path:path>')
# def catch_all(path):
#     if path:
#         print(base_url + '/' + uri + '/{}'.format(path))
#         post_data = {
#             "buildNo": "286",
#             "type": "ios",
#             "version": "1.0.10",
#         }
#         response = requests.post(base_url + '/' + uri + '/{}'.format(path), data=post_data)
#         return response.text
#     return random_number


@msp_interface.route("/newWechat/apply/getAppVersionConfig", methods=["POST", "GET"])
def get_getAppVersionConfig():
    post_data = {
                "buildNo": "286",
                "type": "ios",
                "version": "1.0.10",
            }
    response = requests.post(base_url + '/' + uri + '/{}'.format("/newWechat/apply/getAppVersionConfig"), data=post_data)
    return response.text

@msp_interface.route("/dcs/<string:url>", methods=["GET"])
def get_mspDcs(url):
    print(base_url + '/dcs/{}'.format(url))
    response = requests.get(base_url + '/dcs/{}'.format(url))
    return response.text


