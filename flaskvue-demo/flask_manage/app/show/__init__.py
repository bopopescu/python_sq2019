# -*- coding: utf-8 -*-

# @Time    : 2018/12/4 10:55
# @Author  : songq001
# @Comment : 


from flask import Blueprint


show = Blueprint('show', __name__, static_folder='static')

# 在末尾导入相关模块，是为了避免循环导入依赖，因为在下面的模块中还要导入蓝本show
from . import views, forms
