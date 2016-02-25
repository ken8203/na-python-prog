#! /usr/bin/env python
# -*- coding: utf-8 -*-
# file: split.py

if __name__ == '__main__':
	# root:*:0:0:System Administrator:/var/root:/bin/sh
	with open('/etc/passwd', 'r') as fin:
		for line in fin:
			if line.strip()[0] == '#':
				continue
			data = line.split(':')
			if len(data) < 2:
				continue
			print 'username = {:<15} uid = {}'.format(data[0], data[2])

