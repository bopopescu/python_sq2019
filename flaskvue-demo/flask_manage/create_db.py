# -*- coding: utf-8 -*-

# @Time    : 2018/12/12 17:06
# @Author  : songq001
# @Comment : 


from app import create_app02, db

app = create_app02("testing")

from app.models import Role, OusiGuest, OusiStaff
db.create_all()
