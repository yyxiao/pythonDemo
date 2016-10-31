#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
"""
迭代器
__author__ = xyy
__mtime__ = 2016/10/31
"""

class Account():
    def __init__(self, account_name, account_type, account_cost, return_amount=0):
        self.account_name = account_name
        self.account_type = account_type
        self.account_cost = account_cost
        self.return_amount = return_amount


accounts = [Account('张三', '年费用户', 450.00, 50),
            Account("李四", "月结用户", 100.00),
            Account("杨不悔", "月结用户", 190.00, 25),
            Account("任我行", "月结用户", 70.00, 10),
            Account("凌未风", "年费用户", 400.00, 40)]


# accounts_iterator = iter(accounts)
# print((next(accounts_iterator)).account_name)


class AccountIterator():
    def __init__(self, accounts):
        self.accounts = accounts
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.accounts):
            raise StopIteration('到头了')
        else:
            self.index += 1
            return self.accounts[self.index - 1]

accounts_iterator = AccountIterator(accounts)
# next(accounts_iterator)
# print(list(iter(accounts_iterator)))
# print('test_iterator(next):' + (next(accounts_iterator)).account_name)
for a in accounts_iterator:
    print(a.account_name)
