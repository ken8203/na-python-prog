#! /usr/bin/env python
# -*- coding: utf-8 -*-
# file: na_oop.py

class Employee(object):
    ''' Employee class '''
    
    def __init__(self, name, age, salary):
        self._name = name
        self._age = age
        self._salary = salary
        self._expired_at = None

    def __repr__(self):
    	return '<Employee name={} age={} salary={} expired_at={}>'.format(
                self._name, self._age, self._salary, self._expired_at
    	)

if __name__ == '__main__':
    me = Employee('kcchung', 22, 5000)
    me._salary = 10000
    print me