#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
"""
__author__ = xyy
__mtime__ = 2016/10/25
"""
from collections import OrderedDict

a_dict = {'lee': 100, 'xander': 88, 'tom': 90, 'jessica': 80, 'mary': 70}


def order():
    # 运用collections 中 OrderedDict对dict进行排序
    d = OrderedDict(sorted(a_dict.items(), key=lambda t: t[1], reverse=True))
    print(d)


def knights():
    title = 'Sir'
    title_all = lambda x: title + ' ' + x
    return title_all


act = knights()
print(act('robin'))
order()
L = (lambda x: x+1)(2)
print(L)
