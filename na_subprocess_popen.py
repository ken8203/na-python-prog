#! /usr/bin/env python
# -*-coding: utf-8 -*-
# file: na_subprocess_popen.py

import subprocess

process = subprocess.Popen(
	['base64', '-D'],
	stdin=subprocess.PIPE,
	stdout=subprocess.PIPE
)

output = process.communicate(input=b'cHl0aG9uCg==')[0]
print output
# 'python\n'