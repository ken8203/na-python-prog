#! /usr/bin/env python
# -*-coding: utf8 -*-
# file: na_os_path.py

import os

def list_paths(path):
    paths = []
    for dir_path, dir_names, file_names in os.walk(path):
        for file_name in file_names:
            paths.append(os.path.join(dir_path, file_name))
    return paths

if __name__ == '__main__':
    target = '/etc'
    for path in list_paths(target):
        print path