# -*- coding: utf-8 -*-

# @Time    : 2018/12/14 16:15
# @Author  : songq001
# @Comment : 


from flask import Blueprint

guest = Blueprint('guest', __name__,)

from app.guest import views


