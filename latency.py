#! /usr/bin/env python
# -*- coding: utf-8 -*-
# file: latency.py

if __name__ == '__main__':
	import re
	import sys
	import subprocess

	if len(sys.argv) < 2:
		cmd = 'ping -c 5 linux1.cs.nctu.edu.tw'
	else:
		cmd = 'ping -c 5 %s' % sys.argv[1]

	ping_rquest = subprocess.check_output(cmd, shell=True)

	times = []
	for line in ping_rquest.split('\n'):
		match = re.search('time=(.*?) ms', line)
		if match:
			times.append(float(match.group(1)))

	print 'sum = {:.3f} ms'.format(sum(times))
	print 'max = {:.3f} ms'.format(max(times))
	print 'min = {:.3f} ms'.format(min(times))
