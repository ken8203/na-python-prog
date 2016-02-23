#! /usr/bin/env python
# -*-coding: utf-8 -*-
# file: na_re_search.py

import re

timestamp = 'Sun Mar 24 21:34:34 CST 2016'
r = re.search('\d+:\d+:\d+', timestamp)
print '{}-{} matched: {}'.format(r.start(), r.end(), r.group(0))

r = re.search('(\d+):(\d+):(\d+)', timestamp)
print 'hour=%s, minute=%s, second=%s' % (r.group(1), r.group(2), r.group(3))