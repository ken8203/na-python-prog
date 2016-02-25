#! /usr/bin/env python
# -*- coding: utf-8 -*-
# file: na_try.py

import MySQLdb

try:
    db = MySQLdb.connect(host="localhost", user="root", passwd="db_pass", db="db_name")
except Exception as e:
    print e
else:
    cursor = db.cursor()
    cursor.execute('select * from table')
    rows = cursor.fetchall()
finally:
    db.close()