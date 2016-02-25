#! /usr/bin/env python
# -*- coding: utf-8 -*-
# file: na_numeric.py

import math

# basic usage
print 'type(1) = %s' % type(1)
print 'type(0.1) = %s' % type(0.1)
print 'type(6 + 2j) = %s' % type(6 + 2j)
print '1 + 2 * 3 = {}'.format(1 + 2 * 3)
print '5 / 2 = {}'.format(5 / 2)
print '5 / 2.0 = {}'.format(5 / 2.0)
print '2 ** 3 = {}'.format(2 ** 3)
print '2 ** 100 = {}'.format(2 ** 100)
print '2 ** 0.5 = {}'.format(2 ** 0.5)
print 'abs(-12345) = {}'.format(abs(-12345))
print 'round(math.pi, 3) = {}'.format(round(math.pi, 3))
print

# math library
print 'math.e * math.pi = {}'.format(math.e * math.pi)
print 'math.floor(1.5) = {}'.format(math.floor(1.5))
print 'math.ceil(1.5) = {}'.format(math.ceil(1.5))
print

# bitwise
print '0b101 | 0b10 = {}'.format(0b101 | 0b10)
print '1 << 5 = {}'.format(1 << 5)
print

# complex
x = 6 + 2j
print 'x.imag = {}'.format(x.imag)
print 'x.real = {}'.format(x.real)
print 'x.conjugate() = {}'.format(x.conjugate())

# convertion
print 'int(\'10\') = {}'.format(int('10'))
print 'int(\'0xF\', 16) = {}'.format(int('0xF', 16))
print 'int(\'F\', 16) = {}'.format(int('F', 16))
print 'int(\'10\', 2) = {}'.format(int('10', 2))
print 'hex(256) = {}'.format(hex(256))
print 'oct(256) = {}'.format(oct(256))
print 'bin(256) = {}'.format(bin(256))