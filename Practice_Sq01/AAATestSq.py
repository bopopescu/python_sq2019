# -*- coding: utf-8 -*-

# @Time    : 2018/10/12 16:08
# @Author  : songq001
# @Comment :

import types
import json
import re
import string
import random
import time
from datetime import date, timedelta


# eval()方法二次封装
def eval_str(str_data):
    # eval()对特殊值处理
    null = ""
    true = True
    false = False
    return eval(str_data)


def is_numeric(s):
    s = str(s)
    if s.startswith("-") or s.startswith("+") or "." in s:
        return all(c in "0123456789.+-" for c in s)
    else:
        return all(c in "0123456789" for c in s)

# ==============================================================
# 嵌套json, list的key转成 json_data["A"][0]["name"] 格式，方便直接获取对应key值（类似于jmeter的json插件获取返回结果）
# EG：{"data":{"name":["A", "b"]} --> data.name.0.A
# key中间带有. 情况写法示例：
#  1.{"10.10.10.10": 77777777}  --> ..str(10.10.10.10)
#  2.{"data.policyNo": 88888888}  --> ..data.policyNo
#  3.{"data": {"10.10.10.10": {"A": "aaa"}}}  --> data..str(10.10.10.10)..A
#  4.{"data": {"data.policyNo": {"A": "bbb"}}}  --> data..data.policyNo..A
def get_nestdict_trasKey(self, key_data):
    obj = ""
    if ".." in key_data:  # 处理key中带有.的情况方法2
        for i in key_data.split(".."):
            if i != "":
                if is_numeric(i):
                    obj = "%s[%s]" % (obj, i)
                else:
                    if 'str(' in i:
                        i = i[i.find('(') + 1:-1]
                    obj = "%s['%s']" % (obj, i)
    else:
        for i in key_data.split("."):
            if is_numeric(i):
                obj = "%s[%s]" % (obj, i)
            else:
                if 'str(' in i:
                    i = i[i.find('(') + 1:-1]
                obj = "%s['%s']" % (obj, i)
    return obj


# 获取复杂嵌套list，json对应的下标（key）值, 可以去到任意值
# 格式：keytag： "2.a"      dict_data：[{"a": "111", "b": 222}, "bbbb", {"a": "555", "b": 222}]
def get_nestdict_value(keytag, dict_data):
    """
    :param keytag: 目标key，嵌套则用key1.key2  或者 key1.0.key2
    :param dict_data: 要查询的字典
    :return: 
    """
    if type(dict_data) not in [types.ListType, types.DictType]:
        # dict_data = json.loads(dict_data)
        dict_data = eval_str(dict_data)  # 效果同上
    sname = keytag.strip()
    obj = scmd = realval = ""
    for i in sname.split("."):
        if is_numeric(i):
            obj = "%s[%s]" % (obj, i)
        else:
            if "##" in i:                                   # 处理key中带有.的情况方法1
                i = i.replace("##", ".")
            obj = "%s['%s']" % (obj, i)
    scmd = "%s%s" % ("dict_data", obj)
    try:
        realval = eval(scmd)
    except Exception, e:
        print e.message
        return "[Failed]:cmd change error,eval(%s)" % scmd
    return realval


def get_nestdict_value02(keytag, dict_data):
    """
    :param keytag: 目标key，嵌套则用key1.key2  或者 key1.0.key2
    :param dict_data: 要查询的字典
    :return:
    """
    if type(dict_data) not in [types.ListType, types.DictType]:
        # dict_data = json.loads(dict_data)
        dict_data = eval_str(dict_data)  # 效果同上
    sname = keytag.strip()
    obj = scmd = realval = ""
    if ".." in sname:                                       # 处理key中带有.的情况方法2
        for i in sname.split(".."):
            if i != "":
                if is_numeric(i):
                    obj = "%s[%s]" % (obj, i)
                else:
                    if 'str(' in i:
                        i = i[i.find('(') + 1:-1]
                    obj = "%s['%s']" % (obj, i)
    else:
        for i in sname.split("."):
            if is_numeric(i):
                obj = "%s[%s]" % (obj, i)
            else:
                if 'str(' in i:
                    i = i[i.find('(') + 1:-1]
                obj = "%s['%s']" % (obj, i)
    scmd = "%s%s" % ("dict_data", obj)
    try:
        realval = eval(scmd)
    except Exception as e:
        print e.message
        return "[Failed]:cmd change error,eval(%s)" % scmd
    return realval


def get_nestdict_value03(keytag, dict_data):
    """
    :param keytag: 目标key，嵌套则用key1.key2  或者 key1.0.key2
    :param dict_data: 要查询的字典
    :return:
    """
    if type(dict_data) not in [types.ListType, types.DictType]:
        # dict_data = json.loads(dict_data)
        dict_data = eval_str(dict_data)  # 效果同上
    sname = keytag.strip()
    obj = scmd = realval = ""
    if ".." in sname:                                       # 处理key中带有.的情况方法3
        for i in sname.split(".."):
            if i != "":
                if "." in i:
                    obj = "%s[%s]" % (obj, i)
                else:
                    obj = "%s['%s']" % (obj, i)
    else:
        for i in sname.split("."):
            if is_numeric(i):
                obj = "%s[%s]" % (obj, i)
            else:
                obj = "%s['%s']" % (obj, i)
    scmd = "%s%s" % ("dict_data", obj)
    try:
        realval = eval(scmd)
    except Exception as e:
        print e.message
        return "[Failed]:cmd change error,eval(%s)" % scmd
    return realval

def my_t_01():
    json_t = [{"is_deleted": 0, "subnet_id": None,
               "vpc_info": {"zone_id": "1", "tenant_id": "a7ee782a867c4447b5628a597b165436", "public": True,
                            "project": {"updated_date": "2018-09-14 15:32:34", "status": "active", "is_deleted": 0,
                                        "name": "auto_test", "update_openstack_flag": None,
                                        "tenant_id": "a7ee782a867c4447b5628a597b165436", "enabled": True,
                                        "create_security_group_flag": True, "created_date": "2018-09-14 15:32:31",
                                        "deleted_date": None, "create_openstack_flag": True,
                                        "id": "7c6e89dac1964d79ada8665c5b915c52", "desc": "Auto_自动化测试数据，勿动"},
                            "state": "up", "created_date": "2018-09-14 16:03:01", "cidr": "100.69.4.0/24",
                            "project_id": "7c6e89dac1964d79ada8665c5b915c52", "id": "7cd61f81167f4af4867adca0cfcee0bd",
                            "tenant": {"updated_date": "2018-09-14 15:31:03", "is_deleted": 0, "name": "test",
                                       "enabled": True, "created_date": "2018-09-14 15:30:47",
                                       "desc": "Auto_云管自动化脚本数据，勿动", "id": "a7ee782a867c4447b5628a597b165436",
                                       "cmdb_tenant_id": "ch"}, "name": "auto_test_subordinate"},
               "service_ip": "100.69.4.106", "service_id": "832adc597b1b4051812501edbc7ee6f1",
               "vpc_id": "7cd61f81167f4af4867adca0cfcee0bd", "id": "0ffb8963c3114ec18ab4794ffb485eda"}]
    json_t = eval(str(json_t).strip())
    print type(json_t) in [types.ListType, types.DictType]
    print json_t
    print get_nestdict_value("0.id", json_t)
    print json_t[0]["id"]


def my_t_02():
    """
    关于python2中的unicode和str以及python3中的str和bytes
    https://www.cnblogs.com/yangmingxianshen/p/7990102.html
    :return: 
    """
    my_bytes = 'byte类型'
    print type(my_bytes)
    # str to bytes
    # my_bytes_02 = my_bytes.encode('utf-8')      # 通过encode()把str转成byte  注：python3中的方法， python2报错
    # my_bytes_02 = bytes(my_bytes, encoding='utf8')  # 效果同上    注：python3中的方法， python2报错
    # print type(my_bytes_02)

    # bytes to str
    # my_bytes_03 = my_bytes_02.decode('utf-8')
    # my_bytes_03 = str(my_bytes_02, encoding="utf-8")

    my_bytes_00 = unicode(my_bytes, encoding='utf-8')
    my_bytes_001 = my_bytes.decode('utf-8')  # 效果同上
    print type(my_bytes_00)
    print type(my_bytes_001)
    print type(u'byte类型')
    print my_bytes
    print u'byte类型'


def dcit_te_02():
    dict01 = {"a": 11, "b": 2222}
    print "a" in dict01  # True
    print 2222 in dict01  # False


def dict_handle(dict_data):
    """
    该方法处理json嵌套中，嵌套的json和list是str类型。则需要eval处理。 eg: {"a": "[]"}  --> {"a": []}
    :param dict_data: 
    :return: 
    """
    if type(dict_data) in [types.DictType]:
        for k, v in dict_data.items():
            if type(v) in [types.StringType, types.UnicodeType] and (str(v).startswith("[") or str(v).startswith("{")):
                v1 = eval_str(v)
                dict_data[k] = v1
            else:
                pass
    elif type(dict_data) in [types.ListType]:
        for l in dict_data:
            dict_handle(l)
    return dict_data


def sometest_do_here():
    """
    需要做一些验证的测试，可以写在此方法
    :return:
    """
    contant = {"flag": "Y",
               "applyBarInfo": "[{\"applicantNo\":\"440301199401010636\",\"applyBarCode\":\"1186020001394827\",\"insuredType\":null,\"firstPremium\":\"5170000\",\"applicantName\":\"晓玲\",\"checkReason\":null,\"productName\":\"招商仁和招享人生年金保险（2018）\",\"productCode\":\"2008\",\"applicantType\":\"01\",\"totalNUM\":\"4\",\"insuredNo\":null,\"insuredName\":\"晓玲\",\"relationship\":\"01\"},{\"applicantNo\":\"440301199401010636\",\"applyBarCode\":\"1186020001394928\",\"insuredType\":null,\"firstPremium\":\"5700000\",\"applicantName\":\"晓玲\",\"checkReason\":null,\"productName\":\"招商仁和招享人生年金保险\",\"productCode\":\"2002\",\"applicantType\":\"01\",\"totalNUM\":\"4\",\"insuredNo\":null,\"insuredName\":\"晓玲\",\"relationship\":\"01\"},{\"applicantNo\":\"110101198001010037\",\"applyBarCode\":\"1194040227849439\",\"insuredType\":\"01\",\"firstPremium\":\"2700000\",\"applicantName\":\"皮银一\",\"checkReason\":null,\"productName\":\"招商仁和招享人生年金保险\",\"productCode\":\"2002\",\"applicantType\":\"01\",\"totalNUM\":\"4\",\"insuredNo\":\"110100200301010016\",\"insuredName\":\"银保皮二\",\"relationship\":\"03\"},{\"applicantNo\":\"110101199401010313\",\"applyBarCode\":\"1194040227959340\",\"insuredType\":\"01\",\"firstPremium\":\"3080000\",\"applicantName\":\"杨希\",\"checkReason\":null,\"productName\":\"招商仁和招享人生年金保险\",\"productCode\":\"2002\",\"applicantType\":\"01\",\"totalNUM\":\"4\",\"insuredNo\":\"110101199401011367\",\"insuredName\":\"馁李\",\"relationship\":\"02\"}]"}
    contant00 = "[{\"a\": \"bbbb\"}]"
    print contant00.startswith("[")
    print type(json.loads(contant00))
    print json.loads(json.dumps(contant))  # json.loads() 会把str转成Unicode
    print type(json.loads(json.dumps(contant)))
    print type(contant)
    contant01 = dict_handle(contant)
    print contant01
    print type(contant01)
    print get_nestdict_value("applyBarInfo.0.applyBarCode", contant01)


def sometest_do_here02():
    """
    random测试
    :return:
    """
    print(random.randint(1, 10))        # 产生 1 到 10 的一个整数型随机数
    print(random.random())              # 产生 0 到 1 之间的随机浮点数
    print(random.uniform(1.1, 5.4))     # 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
    print(random.choice('tomorrow'))    # 从序列中随机选取一个元素
    print(random.randrange(1, 100, 2))  # 生成从1到100的间隔为2的随机整数

    a = [1, 3, 5, 6, 7]
    random.shuffle(a)                   # 将序列a中的元素顺序打乱
    print(a)

    print string.ascii_letters, string.digits, type(string.digits)
    print random.choice(string.digits)+random.choice(string.ascii_letters)


def list_removal(v_list):
    """
    list去重
    :param v_list: 
    :return: 
    """
    v_list02 = []
    for v in v_list:
        if v not in v_list02:
            v_list02.append(v)
    return v_list02


def rh_check_result(exceldata, sdic):
    i = str(exceldata).strip().replace("\n", "").replace("”", "\"").replace("‘", "\'").replace("’", "\'").replace(
        "；", ";")
    if ":=" not in i:
        return "input data found error： %s" % i
    sname = i.split(":=")[0].strip()
    # svalue = get_var(str(i.split(":=")[1]).strip())
    svalue = str(i.split(":=")[1]).strip()
    obj = scmd = realval = ""
    sdic_s = sdic
    obj_len = 0
    if ".." in sname:
        for i in sname.split(".."):
            if "." in i:
                obj = "%s[%s]" % (obj, i)
            else:
                obj = "%s['%s']" % (obj, i)

    else:
        sdic_s_len=0
        for i in sname.split("."):
            i = 0 if sname.startswith("*") else i
            print i
            if is_numeric(i):
                obj = "%s[%s]" % (obj, i)
                i = int(i)
            elif i == "*":
                obj_len = sdic_s_len
                obj = "%s[%s]" % (obj, '%s')
                print obj
                i = 0
            else:
                obj = "%s['%s']" % (obj, i)
            sdic_s = sdic_s[i]
            if not isinstance(sdic_s, (bool, int)):
                sdic_s_len = len(sdic_s)
        if obj_len == 0:
            scmd = "%s%s" % ("sdic", obj)
            res = rh_check_value(sdic, scmd, sname, svalue)
        else:
            k = 0
            while k < obj_len:
                obj_k = obj % k
                scmd = "%s%s" % ("sdic", obj_k)
                sname_k = sname.replace('*', str(k))
                res = rh_check_value(sdic, scmd, sname_k, svalue)
                if '[success]' in res:
                    break
                k += 1
    return res

def rh_check_value(sdic, scmd, sname, svalue):
    try:
        realval = eval(scmd)
    except:
        return"[Failed]:cmd change error,eval(%s)" %scmd

    svalue = str(str(svalue).decode("utf-8"))
    realval = str(str(realval).decode("utf-8"))
    if str(svalue.replace("true", "True").replace("false", "False")).strip() == str(realval.replace("true", "True").replace("false", "False")).strip():
        pass
    elif svalue == "不为空":
        if realval == "{}" or realval == "[]":
            return"[Failed]:%s expect is %s,real is %s." %(sname,svalue,realval)
        else:
            return "[success]:%s expect is %s,real is %s." %(sname,svalue,realval)
    elif svalue == "不为0":
        if realval == "0":
            return"[Failed]:%s expect is %s,real is %s." %(sname,svalue,realval)
        else:
            return "[success]:%s expect is %s,real is %s." %(sname,svalue,realval)
    elif svalue == "为空":
        if realval == "{}" or realval == "[]"or realval == '':
            return"[success]:%s expect is %s,real is %s." %(sname,svalue,realval)
        else:
            return "[Failed]:%s expect is %s,real is %s." %(sname,svalue,realval)
    elif svalue == "为0":
        if realval == "0":
            return"[success]:%s expect is %s,real is %s." %(sname,svalue,realval)
        else:
            return "[Failed]:%s expect is %s,real is %s." %(sname,svalue,realval)
    elif svalue.startswith("长度为"):
        len_realval = len(eval(realval))
        len_svalue = int(svalue.replace("长度为", ""))
        if len_realval == len_svalue:
            return "[success]:%s expect is %s,real is %s." % (sname, len_svalue, len_realval)
        else:
            return "[Failed]:%s expect is %s,real is %s." % (sname, len_svalue, len_realval)

    #添加INCLUDE 和EXCEPT结果验证，判断string 中是否存在要查找的关键字
    #示范：resData:=网销保费超过20万元，规则检查不通过<INCLUDE>
    #示范：resData:=投保失败，请重试<EXCEPT>
    elif "<INCLUDE>" in svalue:
        svalue = svalue.split("<")[0]
        if svalue in realval:
            return "[success]:%s expect is %s,real is %s."%(sname,svalue,realval)
        else:
            return "[Failed]:%s expect is %s,real is %s." %(sname,svalue,realval)
    elif "<EXCEPT>" in svalue:
        svalue = svalue.split("<")[0]
        if svalue in realval:
            return "[Failed]:%s expect is %s,real is %s."%(sname,svalue,realval)
        else:
            return "[success]:%s expect is %s,real is %s." %(sname,svalue,realval)

    elif ".00" in realval:
        if svalue == str(realval[:-3]):
            pass
        else:
            return"[Failed]:%s expect is %s,real is %s." %(sname,svalue,realval)
    elif realval == '0.0':
        if svalue in ["0.0","0.00"]:
            pass
        else:
            return"[Failed]:%s expect is %s,real is %s." %(sname,svalue,realval)
    elif svalue == "null":
        if realval == None:
            pass
        else:
            return"[Failed]:%s expect is %s,real is %s." %(sname,svalue,realval)
    elif '\\' in svalue or '\\' in  realval:
        if svalue.decode("unicode-escape")==realval \
                or svalue==realval.decode("unicode-escape") \
                or svalue.decode("unicode-escape")==realval.decode("unicode-escape"):
            pass
        else:
            return"[Failed]:%s expect is %s(%s),real is %s." %(sname,svalue,svalue.decode("unicode-escape"),realval)
    else:
        if svalue == "" and (realval == "[]" or realval == "{}"):
            pass
        else:
            return"[Failed]:%s expect is %s,real is %s." %(sname,svalue,realval)
    return "[success]:%s expect is %s,real is %s." %(sname,svalue,realval)


# dict转成原生form表单格式a=111&b=222          {"a":"a", "bb":"bb"}  --> a=a&bb=bb
def transfor_to_urlencode(dict_data):
    result_str = ""
    tag = "&"
    for (k, v) in dict_data.items():
        result_str = result_str + k + "=" + v + tag
    return result_str[:-1]


# a=111&b=222 原生form表单格式转成dict
def transfor_to_dict(data):
    listdata = data.split("&")
    properties = {}
    for line in listdata:
        if line.find("=") > 0:
            strs = line.replace("\n", "").replace("\t|\n", "").split("=")
            properties[strs[0]] = strs[1]
    return properties



if __name__ == '__main__':
    pass
    # my_t_02()
    # dict_01 = {"pageIndex": "0", "agentNo": "", "pageSize": "10", "posType": "P", "serviceItems": "23", "pip23": {"idNo": "", "policyNo": "", "clientName": "彭"}}
    # print get_nestdict_value("pip23.clientName", dict_01)

    sometest_do_here02()
    print "$g_idcard*2$*".find("*")

    a = +100
    b = -100
    c = '100'
    # print is_numeric(a), is_numeric(b), is_numeric(c)
    i = 'str(3006)'
    print i[i.find('(')+1:-1]

    print type(time.strftime("%Y-%m-%d", time.localtime()))
    print type(date.today())
    print (date.today() + timedelta(days=int(7))).strftime('%Y-%m-%d')

    list0001 = ["运营支持平台建设项目","银保通平台优化项目","研发支持平台","渠道管理平台优化项目","监管平台优化项目","营销支持平台建设项目","研发支持平台","仁和财务平台优化项目","招商金融办公平台","招商金融人力资源管理平台","招商金融财务操作中心平台建设项目","仁和风险管理系统建设项目","招商金融审计数据分析系统项目","云门户","云管平台","云自动化引擎","云存储","云主机","研发支持","研发支持平台","金控监管管理系统","研发支持","客户服务平台建设项目","金科其它研发工作","招融通达项目","金科研发过程改进咨询项目","第三方开放平台","移保通收银台","仁和财务平台优化项目","云主机","金控监管管理系统","研发支持平台","招商金融风险管理平台","招商金融财务操作中心平台建设项目","招商金融人力资源管理平台","仁和财务平台优化项目","仁和财务平台优化项目","仁和财务平台优化项目","运营支持平台建设项目","运营支持平台建设项目","运营支持平台建设项目","运营支持平台建设项目","运营支持平台建设项目","云自动化引擎","仁和风险管理系统建设项目","云管平台","云存储","云备份","云监控","云门户项目","用户接触平台","营销支持平台建设项目","营销支持平台建设项目","营销支持平台建设项目","营销支持平台建设项目","银保通平台优化项目","银保通平台优化项目","渠道管理平台优化项目","渠道管理平台优化项目","监管平台优化项目","招融通达项目","大数据平台建设项目","客户服务平台建设项目","客户服务平台建设项目","在线投保","金科招聘管理系统","仁和在线服务","和宝宝项目","仁和在线服务","法人业务大平台建设项目","法人业务大平台建设项目","法人业务大平台建设项目","海达优智保PC版项目","增值服务管理系统建设项目","集成协作平台","快乐招融","招商金融办公平台","招融通达项目","用户接触平台","集团影像平台","金科招聘管理系统","金科其它研发工作","招商平安资产核心系统建设项目","招商金融人力资源管理平台","招商金融风险管理平台","研发支持平台","快乐招融","招商平安资产核心系统建设项目","招融通达项目","研发支持平台","集成协作平台","集成协作平台","招融通达项目","招融通达项目","营销支持平台建设项目","招商金融办公平台","法人业务大平台建设项目","运营支持平台建设项目"]
    list0002 = list_removal(list0001)
    for k in list0002:
        print k

    json_data00 = {"data": {"aaa": [111, 222]}}
    json_data = {"data": {"10.10.10.10": 1}}
    json_data01 = {"data": {"10.10.10.10": {"A": "aaa"}}}
    json_data011 = {"data": {"data.policyNo": {"A": "bbb"}}}
    json_data02 = {"10.10.10.10": 77777777}
    json_data022 = {"data.policyNo": 88888888}
    print type(json_data)
    # # 方法1
    print get_nestdict_value("data.10##10##10##10.A",json_data01)
    # print get_nestdict_value("10##10##10##10",json_data02)
    # # 方法2
    print get_nestdict_value02("data.aaa.1", json_data00)
    print get_nestdict_value02("data..str(10.10.10.10)..A", json_data01)
    print get_nestdict_value02("data..data.policyNo..A", json_data011)
    print get_nestdict_value02("..str(10.10.10.10)", json_data02)
    print get_nestdict_value02("..data.policyNo", json_data022)
    print "==========="
    print get_nestdict_value03("..data.policyNo", json_data022)
    # # 方法3
    print get_nestdict_value03("data..'10.10.10.10'..A", json_data01)
    # print get_nestdict_value03("..'10.10.10.10'", json_data02)

    # 场景1
    # exceldata = "data.*.a:=1000"
    # sdic = {"data": [{"a":2000, "b":4000, "c":3000}, {"a":1000, "b":2000},  {"a":1000, "c":2000}]}
    # 场景2
    exceldata = "*.a:=1000"
    sdic = [{"a":1000, "b":4000, "c":3000}, {"a":1100, "b":2000},  {"a":1000, "c":2000}]
    # 场景3
    # exceldata03 = "*:=1000"
    # sdic03 = [2000,1000,5000]
    # print rh_check_result(exceldata, sdic)
    # print rh_check_result(exceldata03, sdic03)

    data_dict = {"a": "a", "bb": "bb", "kkk": "我知道了"}
    print transfor_to_urlencode(data_dict)

    data_str = "categoryId=2&cityId=76&bussId=&couponCategory=&merchantTag=&flag=2&latitude=22.559369775870646&longitude=114.0797922139896&pageIndex=1&pageSize=10&regionId=&storeName=&merId=&brand="
    print transfor_to_dict(data_str)

