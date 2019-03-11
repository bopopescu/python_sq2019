# -*- coding: utf-8 -*-

# @Time    : 2018/12/6 16:30
# @Author  : songq001
# @Comment : 


from . import staff
from app.models import OusiStaff



@staff.route('/')
def index():
    return "This is staff web!"


@staff.route('/queryStaff/<int:sid>', methods=['GET', 'POST'])
def query_staff(sid):
    # staffs = OusiStaff.query.all()
    staffs = OusiStaff.query.filter_by(sid=sid).first()
    print(staffs.name)
    return staffs.name

