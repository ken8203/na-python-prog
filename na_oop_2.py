#! /usr/bin/env python
# -*- coding: utf-8 -*-
# file: na_oop_2.py

class Employee(object):
    ''' Employee class '''
    
    __company = 'NCTU'
    __boss = ['Mike', 'Alice', 'Bob']
    def __init__(self, name, age, salary):
        self._name = name
        self._age = age
        self._salary = salary
        self._expired_at = None

    def annual_salary(self):
        return self._salary * 13.5

    @staticmethod
    def check_boss(name):
        if name in Employee.__boss:
        	print '{} is one of our boss.'.format(name)
        else:
        	print '{} is not one of our boss.'.format(name)

    @classmethod
    def visit(cls, name):
    	print 'Hi {}, you are now at {}.'.format(name, cls.__company)

    def __repr__(self):
    	return '<Employee name={} age={} salary={} expired_at={}>'.format(
                self._name, self._age, self._salary, self._expired_at
    	)

class Manager(Employee):
    ''' NCTU Manager '''
    def __init__(self, name, age, salary, group):
        super(Manager, self).__init__(name, age, salary)
        self._group = group

    # overide
    def annual_salary(self):
        return self._salary * 20

    def __repr__(self):
        return '<Manager name={} age={} salary={} expired_at={} group={}>'.format(
                self._name, self._age, self._salary, self._expired_at, self._group
        )


if __name__ == '__main__':
    me = Manager('kcchung', 22, 10000, 'www')
    print me.annual_salary()
