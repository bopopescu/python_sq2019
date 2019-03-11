# -*- coding: utf-8 -*-

# @Time    : 2018/12/6 16:29
# @Author  : songq001
# @Comment : 


from flask import Blueprint

dept = Blueprint('dept', __name__,)

from app.dept import views

