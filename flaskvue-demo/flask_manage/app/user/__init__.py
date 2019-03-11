# -*- coding: utf-8 -*-

# @Time    : 2018/12/6 16:30
# @Author  : songq001
# @Comment : 



from flask import Blueprint

user = Blueprint('user', __name__,)

from app.user import views
