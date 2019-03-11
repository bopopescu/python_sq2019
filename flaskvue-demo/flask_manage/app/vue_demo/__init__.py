# -*- coding: utf-8 -*-

# @Time    : 2018/12/25 16:00
# @Author  : songq001
# @Comment : 


from flask import Blueprint

vue_demo = Blueprint('vue_demo', __name__,)

from app.vue_demo import views

