# -*- coding: utf-8 -*-

# @Time    : 2019/02/02 16:51
# @Author  : songq001
# @Comment : 

import requests
import re
import json



base_jinkog = "http://jzhongb.jzbncp.com"
base_Pa = "https://rmb.pingan.com.cn"           # 平安查询加油站的url
base_Pa02 = "https://pabo2o.pingan.com.cn"      # 平安查询加油站城市列表的url


# 平安加油站         storeName:营口
url_oil = "/mall/o2o/cust/coupon/get_storelist.do"
data_oil = {'cityId': '94', 'pageIndex': '1', 'merchantTag': '', 'pageSize': '1000', 'storeName': '', 'bussId': '', 'brand': '', 'regionId': '', 'longitude': '114.0797922139896', 'latitude': '22.559369775870646', 'flag': '2', 'couponCategory': '', 'categoryId': '2', 'merId': ''}

# 平安查询加油88折城市id
url_cityId = "/m/api/admin/GetCityList.do?type=1"
data_cityId = {}

# 金控商户查询
url_jk_shanghu = "/jinzhongbao/jzb_wx/merchant/checkMerc.do?timestamp=1547714569041&openId=oXg_W1WIvuQ3rPNJ_z29vcjaeO3c"
data_jk_shanghu = {}
# 金控-根据省份获取城市列表     省份代码：广东：2194   湖南：2043   广西：2361   北京：2  江苏：912

url_jk_city = "/jinzhongbao/jzb_wx/merchant/cityList.do?provId=2194"
data_jk_city = {}
# 金控-获取对应省份城市加油商户           上海：provId=889&cityId=890
url_jk_oil = "/jinzhongbao/jzb_wx/merchant/mercNameList.do"
# data__jk_oil = {}
data_jk_oil = {"provId": 889, "cityId": 890, "mcc": 5541}
Cookie = {"JSESSIONID": "E7FF326B1BAF01BB5AFDD950FC0CE181", "new_wx_openid_jzhongb": "oXg_W1WIvuQ3rPNJ_z29vcjaeO3c", "BIGipServerpool_SD_JinZhongBao_NEW": "3338752010.37926.0000", "BIGipServerpool_SD_JinZhongBao_NEW_Nginx": "1258377482.39455.0000"}



def http_requests(base_url, model_url, data, methood="post", cookies={}):
    if methood == "get":
        response = requests.get(base_url+model_url, params=data)
    else:
        response = requests.post(base_url + model_url, data=data, cookies=cookies)
    # response01 = requests.post(base_url+url, data=data)
    return response.text


def get_jk_data(data_str, pattern):
    result_list = []
    data_str = json.loads(data_str)
    data = data_str.get("data")
    for i in data:
        if pattern in i.get("IDENAME"):
            result_list.append(i.get("IDENAME"))
    return str(result_list).decode("unicode-escape")



if __name__ == '__main__':

    # Cookie = {"JSESSIONID": "E7FF326B1BAF01BB5AFDD950FC0CE181", "new_wx_openid_jzhongb": "oXg_W1WIvuQ3rPNJ_z29vcjaeO3c", "BIGipServerpool_SD_JinZhongBao_NEW": "3338752010.37926.0000", "BIGipServerpool_SD_JinZhongBao_NEW_Nginx": "1258377482.39455.0000"}
    # data_jk_oil = {"provId": 2194, "cityId": 2253, "mcc": 5541}
    # response = http_requests(base_jinkog, url_jk_oil, data_jk_oil, methood="post", cookies=Cookie)
    # print response
    # print get_jk_data(response, u"中")
    #
    # data_oil = {'storeName': '', 'cityId': '83', 'pageIndex': '1', 'merchantTag': '', 'pageSize': '1000', 'bussId': '',
    #             'brand': '', 'regionId': '', 'longitude': '114.0797922139896', 'latitude': '22.559369775870646',
    #             'flag': '2', 'couponCategory': '', 'categoryId': '2', 'merId': ''}
    # response01 = http_requests(base_Pa, url_oil, data_oil)
    # print response01


    s = "\xe7\x9a\xae\xe7\x8b\x97\xe7\xab\x8b\xe8\x80\xb3\xe5\xba\xa6\xe6\xb3\x95"
    s1 = "皮狗立耳度法"
    l1 = ["嗷嗷啊", "1", ""]
    print type(s)
    print s
    print type(s1)
    print s1
    ss = ","
    ss1 = ""
    # for i in l1:
        # ss = ss + i + ss
        # ss1 = ss.join(l1)
    # print ss[1:-1]
    print str(l1).decode('string_escape').replace("啊", "呜呜")       # unicode反编码decode("unicode_escape")  ； str反编码：decode('string_escape')
    print type(repr(l1))
    print ss1

    print repr('你好')
    print repr('你好').decode('string_escape')
    print str('你好')
    print "你好".encode("string-escape")

    import sys
    reload(sys)
    sys.setdefaultencoding('gbk')
    print sys.getdefaultencoding()
    aa = '\\xC1\\xBD'
    bb = aa.decode("string_escape")             # encode("string_escape") 是把中文转为16进制，decode('string_escape')是去掉转义且把16进制反编码为中文
    print bb

    a = open("A.txt", "wb+")
    a.write(str(s))

    tup1 = ('physics', 'chemistry', 1997, 2000)
    print tup1[1]

