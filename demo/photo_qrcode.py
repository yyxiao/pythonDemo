#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
"""
__author__ = xyy
__mtime__ = 2016/8/25
"""
import os
from pyramid.response import Response
import qrcode
from PIL import Image
from io import BytesIO


def room_qrcode(request):
    """
    生成带logo的二维码
    :return:
    """
    url = 'http://baidu.com'
    room_id = request.GET.get('room_id', '0')
    user_id = request.session['userId']
    json1 = {
        'url': url,
        'room_id': room_id,
        'user_id': user_id
    }
    img = qrcode.make(json1)
    img = img.convert("RGBA")
    # datas = img.getdata()
    # newData = []
    # for item in datas:
    #     if item[0] == 0 and item[1] == 0 and item[2] == 0:
    #         newData.append((8, 99, 190, 0))
    #     else:
    #         newData.append(item)
    # img.putdata(newData)
    # # 改变颜色结束
    # buf = BytesIO()
    # img.save(buf, 'jpeg')
    # 读取本地图片
    logo = 'E://yy.jpg'
    if logo and os.path.exists(logo):
        try:
            icon = Image.open(logo)
            img_w, img_h = img.size
        except Exception as e:
            print(e)
    factor = 4
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)
    icon_w, icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

    w = int((img_w - icon_w) / 2)
    h = int((img_h - icon_h) / 2)
    icon = icon.convert("RGBA")
    img.paste(icon, (w, h), icon)
    buf = BytesIO()
    img.save(buf, 'jpeg')
    image_stream = buf.getvalue()
    response = Response(
        image_stream,
        request=request,
        content_type='image/png'
    )
    return response
