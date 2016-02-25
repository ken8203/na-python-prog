#! /usr/bin/env python
# -*- coding: utf-8 -*-
# file: myip.py

if __name__ == '__main__':
	import re
	import requests

	url = 'https://myip.com.tw/'
	r = requests.get(url)
	body = r.text

	pattern = r'<font color=green>(\d+\.\d+\.\d+\.\d+)</font>'
	match = re.search(pattern, body)
	if match:
		print 'Your IP is %s' % match.group(1)
	else:
		print 'Something goes wrong.'

