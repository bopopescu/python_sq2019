# -*- coding: utf-8 -*-

# @Time    : 2018/12/14 16:16
# @Author  : songq001
# @Comment : 



from flask import Blueprint

staff = Blueprint('staff', __name__,)

from app.staff import views
