#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
"""
__author__ = xyy
__mtime__ = 2016/10/26
"""

import urllib
import json

Test_Token = '_37MX1Gj75oM4Az98V3oz8fQVqK2OmnEBhQYKwhkoLMcluwZ4NyNlMd0QJtgrUUt2uKyT8A_RhbFuaguZIqSgL0sJ2gmdNfLGsogE0q9ORO-7dPzTVQnQpHrO13NdPtGYJUgAJAOZK'
AppID = "wx0eb03bdabc236f8e"
AppSecret = "a3978d234121ae5876b38206bdd8583b"
# AppID = "wx0eb03bdabc236f8e"
# AppSecret = "a3978d234121ae5876b38206bdd8583b"
API_URL = 'https://api.weixin.qq.com/'
OPEN_URL = 'https://open.weixin.qq.com/'
WX_TOKEN = API_URL + 'cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s'
WX_AUTHORIZE = OPEN_URL + 'connect/oauth2/authorize?appid=%s&redirect_uri=%s&response_type=code&scope=%s&state=%s#wechat_redirect'
WX_CODE_TOKEN = API_URL + 'sns/oauth2/access_token?appid=%s&secret=%s&code=%s&grant_type=authorization_code'


class Wechat:
    def __init__(self):
        self

    @staticmethod
    def access_token():
        """
        get获取access_token
        :return:
        """
        req = urllib.request.Request(url=WX_TOKEN % (AppID, AppSecret))
        req.add_header('Accept', 'application/json')
        url_response = urllib.request.urlopen(req)
        return url_response.read()

    @staticmethod
    def authorize():
        """
        oauth登录
        跳转redirect_uri/?code=CODE&state=STATE。
        :return:
        """
        req = urllib.request.Request(url=WX_AUTHORIZE % (AppID, 'https://www.baidu.com','snsapi_base', 's'))
        req.add_header('Accept', 'application/json')
        url_response = urllib.request.urlopen(req)
        return url_response.read()

    @staticmethod
    def code_token():
        """
        oauth登录
        跳转redirect_uri/?code=CODE&state=STATE。
        :return:
        """
        req = urllib.request.Request(url=WX_CODE_TOKEN % (AppID, AppSecret, '011Zk1b01iieP12Vvdb01B57b01Zk1bf&state=123'))
        req.add_header('Accept', 'application/json')
        url_response = urllib.request.urlopen(req)
        return url_response.read()

token = Wechat.access_token().decode('utf-8')
openid = Wechat.code_token().decode('utf-8')
print(token)
print(openid)
# print('token' + eval(token))
# print('openid' + eval(openid))
# cope = Wechat.authorize()
# 转为json输出
print(json.loads(token))
print(json.loads(openid))
"""
{"access_token":"jRQFPl5SeNBe-6YpmWzyyEcb4et2Cctwciwsaxt5hnGraDH7Ham39efrajBL7jCPV7447649XfZGXYQ7OQ3aTOZBquqXyelz6W9YaPQaOVoQVXdADACHJ","expires_in":7200}
{"access_token":"M_ehSK0iARNACeQ6iyNPxln-7Npf1p1POAjeqlYKL0qRbMwfZF0HwL14A9iE7v32VlJnY9JTd5IQFWhHf0IQBNxBSYUH_475grJTvKXuqdA","expires_in":7200,"refresh_token":"kzh5zQ1y3KeRr2dubJ_eIUInt1mP69ZnFa82OXzEveFJIm5PawgEYeT9KUUi-wmGTdtvs3_4qcEK-umQPnBp_xq_h4YaIthXM0xCfn2se3g","openid":"o6zKAuAN59AAT8jcfwjIqxHUafQs","scope":"snsapi_base"}
{'expires_in': 7200, 'access_token': 'jRQFPl5SeNBe-6YpmWzyyEcb4et2Cctwciwsaxt5hnGraDH7Ham39efrajBL7jCPV7447649XfZGXYQ7OQ3aTOZBquqXyelz6W9YaPQaOVoQVXdADACHJ'}
{'expires_in': 7200, 'openid': 'o6zKAuAN59AAT8jcfwjIqxHUafQs', 'access_token': 'M_ehSK0iARNACeQ6iyNPxln-7Npf1p1POAjeqlYKL0qRbMwfZF0HwL14A9iE7v32VlJnY9JTd5IQFWhHf0IQBNxBSYUH_475grJTvKXuqdA', 'scope': 'snsapi_base', 'refresh_token': 'kzh5zQ1y3KeRr2dubJ_eIUInt1mP69ZnFa82OXzEveFJIm5PawgEYeT9KUUi-wmGTdtvs3_4qcEK-umQPnBp_xq_h4YaIthXM0xCfn2se3g'}
获取成功
"""

if token:
    print("获取成功")
