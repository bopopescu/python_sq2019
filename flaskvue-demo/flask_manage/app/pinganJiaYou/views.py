# -*- coding: utf-8 -*-

# @Time    : 2018/12/6 16:30
# @Author  : songq001
# @Comment : 


from . import pinganJiaYou
from flask import jsonify, redirect, request, render_template
from app import db
from app.models import Role
import requests
from config import Config


pingAn_url = Config.pingAn


@pinganJiaYou.route('/')
def index():
    return "This is pinganJiaYou web!"


# 获取城市ID
@pinganJiaYou.route('/admin/GetCityList.do', methods=['GET', 'POST'])
def GetCityList():
    data = {
                "type": "1"
            }
    response = requests.get(pingAn_url + '/{}'.format("/admin/GetCityList.do"), params=data)
    return response.text

# 获取平安加油站
@pinganJiaYou.route('/merchant/storeList.do', methods=['GET', 'POST'])
def add_role():
    print(request.headers)
    if request.method == 'GET':
        return "addRole get!"
    else:
        p_id = request.form['id']
        p_role = request.form['role']

        if not p_id:
            return 'id 不能为空'
        elif not p_role:
            return 'role 不能为空'
        newobj = Role(id=p_id, role=p_role)
        try:
            db.session.add(newobj)
            db.session.commit()
            new_data = Role.query.filter_by(id=p_id).first()
            return "新增成功: " + str((new_data.id, new_data.role))
        except Exception as e:
            return str(e)


@pinganJiaYou.route('/search')
def search():
    print (request.args)        # get请求，打印url后面所有的参数（key:value形式），如果有多个参数，通过request.args.get('key')的方式获取值
    return render_template('role/search.html')


@pinganJiaYou.route('/login')
def login():
    if request.method == 'GET':                         # 此处判断get和post方法与django相同
        return render_template('role/login.html')
    else:
        username = request.form.get('username')         # post请求。获取模版语言中输入框输入的值
        password = request.form.get('password')

        return "post request, username: %s password:%s" % (username,password)



