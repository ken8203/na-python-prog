#! /usr/bin/env python
# -*-coding: utf8 -*-
# file: na_csv.py

import csv

with open('file.csv', 'r') as fin:
    for line in csv.reader(fin):
        print line