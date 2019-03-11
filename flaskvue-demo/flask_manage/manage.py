# -*- coding:utf-8 -*-

# @Time    : 2018/12/04 10:22
# @Author  : songq001
# @Comment : 启动程序

from app.dept import dept
from app.user import user
from app.role import role
from app.guest import guest
from app.staff import staff
from app.vue_demo import vue_demo
from app.msp_interface import msp_interface
from flask import Flask
from flask_script import Manager, Shell
from flask_migrate import Migrate
from config import config
from flask_sqlalchemy import SQLAlchemy
from app import create_app02, db
import os


# 需要加载的蓝图
blue_show = [dept, user, role, guest, staff, vue_demo, msp_interface]

app = create_app02(os.getenv('FLASK_CONFIG') or 'testing')
manager = Manager(app)
# migrate = Migrate(app, db)

# def make_shell_context():
#     return dict(app=app, db=db)


# manager.add_command("shell", Shell(make_context=make_shell_context))


app.config['JSON_AS_ASCII'] = False           # 让jsonify返回的json串支持中文显示

# 注册蓝图
for blue_s in blue_show:
    app.register_blueprint(blue_s, url_prefix='/{}'.format(str(blue_s.name)))


# ========建表====================================
# from app import create_app02, db
#
# app = create_app02("testing")
# ========建表 END====================================

if __name__ == '__main__':
    # app.run()
    manager.run()
    #  建表
    # from app.models import Role, OusiGuest, OusiStaff
    # db.create_all()


