import random
from tools.api import request_tool

import pytest
from tools.data import random_tool
from tools.report import log_tool

from tools.tools.time import open,open1

o = open()
op = open1()
t = random_tool.random_gbk_chines()


d = {}
b = {}
l = {}

def test_post_json(pub_data):  # 上报案件
    method = "POST"  # 请求方法，全部大写
    feature = "案件管理"  # allure报告中一级分类
    story = '案件发现'  # allure报告中二级分类
    title = "待受理-上报案件"  # allure报告中用例名字
    uri = f'/api/web/events/report-message?id=false&token={pub_data["token"]}'  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {
        'reportContent': '{"city":"上海","district":20,"eventName":"阻塞消防通道的违规行为","eventDescription":"玩のfrv","street":"0","source":"1","degree":"1","community":null,"address":"王二狗","addressNote":"无二等分v吧","grid_center":"2020155","audios":[],"videos":[],"scenes":[],"result":[],"areaType":"1","eventType":{"level_1":"事件","level_2":"设施管理","level_3":"违规占用地下公共人行通道"},"lngCd":0,"latCd":0}',
        'handleChannel': '3',
        'type': '1'
    }

    status_code = 200  # 响应状态码
    expect = "200"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, data=data,
                             status_code=status_code, expect=expect, feature=feature, story=story, title=title)
    log_tool.info('----------------------上报成功---------------------')
    assert r.json()["code"] == 200 and r.json()["data"] == True  # 断言


def test_get_params(pub_data):  # 查询待受理案件列表
    method = "GET"  # 请求方法，全部大写
    feature = "案件管理"  # allure报告中一级分类
    story = '案件发现'  # allure报告中二级分类
    title = "待受理-查询案件"  # allure报告中用例名字
    uri = f"/api/web/events/report-list?start={open()}&end={open1()}&pageSize=10&page=1&sort=event_time&sort_type=0&isResolve=0&token={pub_data['token']}"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    # params = {"phone":'18103909786'}
    headers = {'Accept': 'application/json, text/plain, */*', 'Content-Type': 'application/json;charset=UTF-8'}
    status_code = 200  # 响应状态码
    expect = "200"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, status_code=status_code, expect=expect,
                             feature=feature, story=story, title=title, headers=headers)
    j = r.json()
    p = j['data']['items'][0]['eventId']
    #print(p)
    d["eventId"] = p
    assert r.json()["code"] == 200 and r.json()["data"] != None
    log_tool.info('----------------------查询成功----------------------')


def test_accept_and_hear_a_case(pub_data):  # 案件受理
    method = "PATCH"  # 请求方法，全部大写           #
    feature = "案件管理"  # allure报告中一级分类
    story = '案件发现'  # allure报告中二级分类
    title = "待受理-受理"  # allure报告中用例名字
    url = f"/api/web/events/{d['eventId']}?token={pub_data['token']}&id={d['eventId']}"  # 接口地址
    log_tool.info('受理')
    # params = {"phone":'18103909786'}
    headers = {"Content-Type": "application/json;charset=utf-8"}

    data = {"data": {"status": "12", "desc": "同意受理！", "withNext": 0, "nextDesc": ""}}

    status_code = 200  # 响应状态码
    expect = "200"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=url, pub_data=pub_data, status_code=status_code, headers=headers,
                             expect=expect, feature=feature, story=story, title=title, json_data=data)
    p=r.json()
    t=p['data']['eventId']
    b["eventId"]=t
    #print(t)
    assert r.json()["code"] == 200 and r.json()["data"] != None

    log_tool.info('----------------------受理成功----------------------')

def test_get_register(pub_data):  #立案
    method = "PUT"  #请求方法，全部大写
    feature = "案件管理"  # allure报告中一级分类
    story = '案件立案'  # allure报告中二级分类
    title = "待立案-立案操作"  # allure报告中用例名字
    uri = f"/api/web/events/{b['eventId']}?token={pub_data['token']}&id={b['eventId']}"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    #params = {"phone":'18103909786'}
    headers = {"Content-Type": "application/json;charset=utf-8"}
    data={"data":{"eventName":"阻塞消防通道的违规行为","address":"王二狗","addressNote":"无二等分v吧","eventDescription":"玩のfrv","eventType":{"level_1":"事件","level_2":"设施管理","level_3":"违规占用地下公共人行通道"},"community":"","source":1,"images":[],"status":13,"confirm_info":{"description":"案件情况属实，予以立案，请派遣处置！"}}}

    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r=request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,json_data=data,
                           expect=expect,feature=feature,story=story,title=title,headers=headers)
    p=r.json()
    p1=p['data']["eventId"]
    l["eventId"]=p1
    print(p1)

    assert r.json()["code"] == 200 and r.json()["data"] != None


    log_tool.info('----------------------立案成功----------------------')


def test_post_json_xiapai(pub_data): #下派
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = f"/api/web/case/dispatch-meta?id={b['eventId']}&token={pub_data['token']}"  # 接口地址

    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {'id': '665180',
            'meta_id': '20001',
            'deps': '[]',
            'deal': '2021-02-28 15:27:30',
            'desc': '请尽快进行处理，并在处理完成后及时反馈。'}
    status_code = 200  # 响应状态码
    expect = "200"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r=request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)

    print(r)





if __name__ == "__main__":
    pytest.main(['-s', 'test_baoan.py'])
