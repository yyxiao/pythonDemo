#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
"""
__author__ = xyy
__mtime__ = 2016/10/28
"""
import re

# 正则匹配电话号码
phone = "13893670000"
p2 = re.compile('^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}')
phonematch = p2.match(phone)

if phonematch:
    print(phonematch.group())
else:
    print("phone number is error!")