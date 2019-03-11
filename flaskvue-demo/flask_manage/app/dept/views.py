# -*- coding: utf-8 -*-

# @Time    : 2018/12/6 16:30
# @Author  : songq001
# @Comment : 


from . import dept
from flask import jsonify, redirect, request
import json
from app import db
from app.models import OusiGuest, OusiStaff, Role


dept_data = [
    {
        'name': '部门1',
        'id': 12345
    },
    {
        'name': '部门2',
        'id': 12346
    }
]


@dept.route('/')
def index():
    # return "This is dept web!"
    resp = jsonify({'error':False})
    # 跨域设置
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@dept.route('/<int:id>', methods=['GET', ])
def get(id):
    for dept in dept_data:
        if int(dept['id']) == id:
            return jsonify(status='success', dept=dept)

    return jsonify(status='failed', msg='dept not found')


@dept.route('/depts', methods=['GET', 'POST'])
def get_depts():
    print("======请求头=======" + "\n" + str(request.headers))
    data = {
        'status': 'success',
        'depts': dept_data
    }

    resp = jsonify(data)
    # 跨域等设置
    resp.headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        # 'Access-Control-Allow-Methods': 'DELETE'
    }
    return resp
    # return json.dumps(data, ensure_ascii=False, indent=1)


@dept.route('/queryGuest/<string:phone>', methods=['GET', 'POST'])
def query_guests(phone):
    # guests = OusiGuest.query.all()
    guests = OusiGuest.query.filter_by(staff_phone=phone).first()
    print(guests.name)
    return guests.name


@dept.route('/queryRole/<int:id>', methods=['GET', 'POST'])
def query_role(id):
    roles = Role.query.filter_by(id=id).first()
    print(roles.role)
    return roles.role

@dept.route('/addRole', methods=['GET', 'POST'])
def add_role():
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



