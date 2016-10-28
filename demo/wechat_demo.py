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
        url_response = urllib.urlopen(WX_TOKEN % (AppID, AppSecret))
        return url_response.read()

    @staticmethod
    def authorize():
        """
        oauth登录
        跳转redirect_uri/?code=CODE&state=STATE。
        :return:
        """
        url_response = urllib.urlopen(WX_AUTHORIZE % (AppID, 'https://www.baidu.com','snsapi_base', 's'))
        return url_response.read()


token = Wechat.access_token()
print(eval(token))
# cope = Wechat.authorize()
# code = Wechat.code_token()
# 转为json输出
print(json.loads(token))

if token:
    print("获取成功")