# -*- coding: utf-8 -*-

# @Time    : 2018/12/6 16:30
# @Author  : songq001
# @Comment : 


from . import guest
from flask import jsonify, redirect, request
from app.models import OusiGuest



@guest.route('/')
def index():
    return "This is guest web!"


@guest.route('/queryGuest/<string:phone>', methods=['GET', 'POST'])
def query_guests(phone):
    # guests = OusiGuest.query.all()
    guests = OusiGuest.query.filter_by(staff_phone=phone).first()
    print(guests.name)
    return guests.name





