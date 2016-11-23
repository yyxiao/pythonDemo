# -*- coding:utf-8 -*-  
"""
Create on 16/11/22
Author xiaoyy
"""

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
            sql = 'select * from boohee'
            # 获取查询结果
            cursor.execute(sql)
            data = cursor.fetchone()
            for key, value in list(six.iteritems(data)):
                if isinstance(value, (bytearray, six.binary_type)):
                    # data[key] = value.decode('utf8')
                    # 作用同上
                    data[key] = utils.text(value)
            if 'result' in data:
                data['result'] = json.loads(data['result'])
            print(data)
            """
            {'url': 'http://www.boohee.com/shiwu/niuru_junzhi', 'taskid': '0137f12ec1348158a407f5fb622c64c7',
            'updatetime': 1479816033.2923,
            'result': {
                'url': 'http://www.boohee.com/shiwu/niuru_junzhi',
                'title': '牛奶的热量，牛奶减肥 - 薄荷食物库',
                'content': {'value': '含量(每100毫升) 含量(每100毫升) 54.00 3.40 3.20 3.00 0.00 24.00', 'name': '营养素 营养素 热量(大卡) 碳水化合物(克) 脂肪(克) 蛋白质(克) 纤维素(克) 维生素A(微克)'},
                'contents': '营养素 含量(每100毫升) 营养素 含量(每100毫升) 热量(大卡) 54.00 碳水化合物(克) 3.40 脂肪(克) 3.20 蛋白质(克) 3.00 纤维素(克) 0.00 维生素A(微克) 24.00 维生素C(毫克) 1.00 维生素E(毫克) 0.21 胡萝卜素(微克) 一 硫胺素(毫克) 0.03 核黄素(毫克) 0.14 烟酸(毫克) 0.10 胆固醇(毫克) 15.00 镁(毫克) 11.00 钙(毫克) 104.00 铁(毫克) 0.30 锌(毫克) 0.42 铜(毫克) 0.02 锰(毫克) 0.03 钾(毫克) 109.00 磷(毫克) 73.00 钠(毫克) 37.20 硒(微克) 1.94 >> 详细'
                }
            }

            """
        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        connection.commit()
    finally:
        connection.close()


# search_blob_demo()
