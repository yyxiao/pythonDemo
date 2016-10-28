#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
"""
__author__ = xyy
__mtime__ = 2016/10/11
"""
import urllib
import json

AppID = "wx791bc67ef3987498"
AppSecret = "916b6268e54b5f0b03e95214b74c880b"
API_URL = 'https://api.weixin.qq.com/'
OPEN_URL = 'https://open.weixin.qq.com/'
WX_TOKEN = API_URL + 'cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s'
WX_AUTHORIZE = OPEN_URL + 'connect/oauth2/authorize?appid=%s&redirect_uri=%s&response_type=code&scope=%s&state=%s#wechat_redirect'
WX_CODE_TOKEN = API_URL + 'sns/oauth2/access_token?appid=%s&secret=%s&code=%s&grant_type=authorization_code'


class Weixin:
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

    @staticmethod
    def code_token():
        """
        oauth登录
        跳转redirect_uri/?code=CODE&state=STATE。
        :return:
        """
        url_response = urllib.urlopen(WX_CODE_TOKEN % (AppID, AppSecret, '031aA8ou1QD7x70pC9ou1AR4ou1aA8oc&state='))
        return url_response.read()


if __name__ == '__main__':
    token = Weixin.access_token()
    cope = Weixin.authorize()
    code = Weixin.code_token()
    # 转为json输出
    print(json.loads(token))
    if token:
        print("获取成功")