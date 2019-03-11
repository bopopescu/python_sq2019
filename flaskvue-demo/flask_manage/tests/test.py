# -*- coding: utf-8 -*-

# @Time    : 2018/12/7 16:27
# @Author  : songq001
# @Comment : 单元测试


import requests
import cx_Oracle


# base_url = "http://127.0.0.1:8080"
#
# url = "/hello"
# # url = "/role/addRole"
#
# data = {}
# # data = {"id":"9", "role":"guncun05"}
#
# headers = {'Content-Type': 'application/x-www-form-urlencoded'}
# response = requests.get(base_url + url, data=data, headers=headers)
# # response = requests.post(base_url + url, data=data)
#
# print(response.headers)             # 'Content-Type': 'text/html; charset=utf-8'
# print(response.text)


def conn_oracle():
    connstr = "dbmgr/zhaoshang001@100.69.236.58:1634/slis"
    conn = cx_Oracle.connect(connstr)
    cursor = conn.cursor()


conn_oracle()

