# -*- coding:utf-8 -*-  
"""
Create on 16/11/24
Author xiaoyy
"""
import datetime
from openpyxl import Workbook
import pymysql
import json
import six
from pyspider.libs import utils


def search_blob_demo():
    # 连接配置信息
    mysql_config = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': 'root',
        'db': 'resultdb',
        'charset': 'utf8',
        'cursorclass': pymysql.cursors.DictCursor,
    }
    # 创建连接
    connection = pymysql.connect(**mysql_config)
    # 执行sql语句
    try:
        with connection.cursor() as cursor:
            # 执行sql语句，进行查询
            sql = 'select * from boohee limit 10'
            # 获取查询结果
            cursor.execute(sql)
            # data = cursor.fetchone()
            data = cursor.fetchall()
            wb = Workbook()
            # 激活 worksheet
            ws = wb.active
            for i in range(len(data)):
                for key, value in list(six.iteritems(data[i])):
                    if isinstance(value, (bytearray, six.binary_type)):
                        # data[key] = value.decode('utf8')
                        # 作用同上
                        data[i][key] = utils.text(value)
                if 'result' in data[i]:
                    data[i]['result'] = json.loads(data[i]['result'])
                # print(data)
                contents = data[i]['result']['contents'].split('>>')[0].strip().split(' ')[2:]
                # print(len(contents))
                # 可以附加行，从第一列开始附加
                ws.append(contents)
            # 保存文件
            wb.save("sample.xlsx")

        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        connection.commit()
    finally:
        connection.close()

search_blob_demo()
