#! /usr/bin/env python
# -*-coding: utf-8 -*-
# file: na_requests.py

import re
import requests

url = 'https://www.ptt.cc/bbs/Gossiping/M.1456150026.A.855.html'
r = requests.get(url, cookies={'over18': '1'})

import re
title = re.findall('<title>(.*?)</title>', r.text)[0]
print title
# [問卦] 台大如果有妹妹系要幾級分? - 看板 Gossiping - 批踢踢實業坊