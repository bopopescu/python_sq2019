# -*- coding: utf-8 -*-

# @Time    : 2018/12/6 16:30
# @Author  : songq001
# @Comment : 


from . import role
from flask import jsonify, redirect, request, render_template
from app import db
from app.models import Role



@role.route('/')
def index():
    return "This is role web!"


@role.route('/queryRole/<int:id>', methods=['GET', 'POST'])
def query_role(id):
    roles = Role.query.filter_by(id=id).first()
    print(roles.role)
    return roles.role

@role.route('/addRole', methods=['GET', 'POST'])
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


@role.route('/search')
def search():
    print (request.args)        # get请求，打印url后面所有的参数（key:value形式），如果有多个参数，通过request.args.get('key')的方式获取值
    return render_template('role/search.html')


@role.route('/login')
def login():
    if request.method == 'GET':                         # 此处判断get和post方法与django相同
        return render_template('role/login.html')
    else:
        username = request.form.get('username')         # post请求。获取模版语言中输入框输入的值
        password = request.form.get('password')

        return "post request, username: %s password:%s" % (username,password)


@role.route('/add/',methods=['GET','POST'])
def add():
    if request.method == 'POST':
        p_id = request.form.get('id',None)
        p_role = request.form.get('role',None)

        if not p_id or not p_role:
            return 'input error'

        newobj = Role(id=p_id, role=p_role)
        try:
            db.session.add(newobj)
            db.session.commit()
            # new_data = Role.query.filter_by(id=p_id).first()
            roles = Role.query.all()
            return render_template('role/add.html',roles=roles)
        except Exception as e:
            return str(e)
    roles = Role.query.all()
    return render_template('role/add.html',roles=roles)

