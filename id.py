#! /usr/bin/env python
# -*- coding: utf-8 -*-
# file: id.py

table = dict(
	A=10, B=11, C=12,
	D=13, E=14, F=15,
	G=16, H=17, I=34,
	J=18, K=19, L=20,
	M=21, N=22, O=35,
	P=23, Q=24, R=25,
	S=26, T=27, U=28,
	V=29, W=32, X=30,
	Y=31, Z=33
)

def check(id_num):
	digit = table[id_num[0].upper()]
	check_sum = digit / 10.0 + digit % 10 * 9
	check_sum += sum(int(id_num[i]) * (9-i) for i in range(1, len(id_num)))
	check_sum += int(id_num[9])
	return check_sum % 10 == 0

if __name__ == '__main__':
	import re

	while True:
		id_number = raw_input('Please enter your id number: ')

		if not re.search('^[A-Za-z]\d{9}$', id_number):
			print 'Wrong format!'
		elif check(id_number):
			print 'Valid id number'
		else:
			print 'Invalid id number'
