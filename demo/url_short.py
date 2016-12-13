# -*- coding:utf-8 -*-  
"""
Create on 16/12/13
Author xiaoyy
"""
from __future__ import with_statement
import contextlib
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

try:
    from urllib.request import urlopen
except ImportError:
    from urllib3 import urlopen
import sys

# 生成tinyurl 通过tinyurl api
def make_tiny(url):
    request_url = ('http://tinyurl.com/api-create.php?'+urlencode({'url':url}))
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8')


if __name__ == '__main__':
    print(make_tiny('https://pythontips.com/2013/08/03/a-url-shortener-in-python/ '))