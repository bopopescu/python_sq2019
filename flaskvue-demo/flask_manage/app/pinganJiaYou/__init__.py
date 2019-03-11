# -*- coding: utf-8 -*-

# @Time    : 2018/12/14 16:21
# @Author  : songq001
# @Comment : 



from flask import Blueprint

pinganJiaYou = Blueprint("pinganJiaYou", __name__,)

from app.pinganJiaYou import views
