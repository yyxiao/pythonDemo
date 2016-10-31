#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
"""
__author__ = xyy
__mtime__ = 2016/10/31
"""


class MyRange:

    def __init__(self, start=0, end=None, step=1):
        if end is None:
            self.index = 0
            self.start = 0
            self.end = start
        else:
            self.index = start
            self.start = start
            self.end = end

        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        self.index += self.step
        if self.start < self.end and not self.start < self.index <= self.end:
            raise StopIteration

        elif self.start > self.end and not self.start > self.index >= self.end:
            raise StopIteration

        return self.index

for i in MyRange(10):
    print(i)
