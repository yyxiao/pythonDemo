# -*- coding: utf-8 -*-
import pypinyin
from pypinyin import pinyin, lazy_pinyin


def main():
    print(pinyin(u'中心'))
    # 启用多音字模式
    print(pinyin(u'中心', heteronym=True))
    # 设置拼音风格
    print(pinyin(u'中心', style=pypinyin.FIRST_LETTER))
    print(pinyin(u'中心', style=pypinyin.TONE2, heteronym=True))
    print(lazy_pinyin(u'测试'))

# 个人感觉貌似默认启动main()
if __name__ == "__main__":
    main()