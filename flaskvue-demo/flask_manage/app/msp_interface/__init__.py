# -*- coding: utf-8 -*-

# @Time    : 2019/01/09 18:02
# @Author  : songq001
# @Comment : 


from flask import Blueprint

msp_interface = Blueprint('msp_interface', __name__,)

from app.msp_interface import views

