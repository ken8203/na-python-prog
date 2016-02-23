#! /usr/bin/env python
# -*-coding: utf-8 -*-
# file: na_re_split_findall.py

import re

timestamp = 'Sun Mar 24 21:34:34 CST 2016'
r = re.split('\W', timestamp)
print r
# ['Sun', 'Mar', '24', '21', '34', '34', 'CST', '2016']

r = re.findall('\w+s', 'raining cats & dogs')
print r
# ['cats', 'dogs']