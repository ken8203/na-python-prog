#! /usr/bin/env python
# -*-coding: utf-8 -*-
# file: na_subprocess_call.py

import subprocess

return_code = subprocess.call(['ls', '-al'])
print return_code
# 0