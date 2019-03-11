# -*- coding: utf-8 -*-

# @Time    : 2018/12/14 16:21
# @Author  : songq001
# @Comment : 



from flask import Blueprint

role = Blueprint("role", __name__,)

from app.role import views
