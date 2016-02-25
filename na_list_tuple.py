#! /usr/bin/env python
# -*- coding: utf-8 -*-
# file: na_list_tuple.py

# basic usage
print 'type([]) = %s' % type([])
print 'type(()) = %s' % type(())
a = [11, 1, 4, 5 ,7]
b = [9, 2, 11]
c = a + b
print 'len(a) = {}'.format(len(a))
print [1] * 5
print 7 in a
print 7 in b
print c.count(11)
print a.index(4)
print a.pop()
print sorted(b)

# index in list
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#	 0  1  2  3  4  5  6  7  8  9
#  -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
#  a[start:stop:step]

print a[2]
print a[-1]
print a[100] # IndexError
print a[:5]
print a[7:]
print 
