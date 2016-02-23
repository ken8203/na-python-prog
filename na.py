#! /usr/bin/env python
# -*- coding: utf8 -*-
# file: na.py

def na(score=None):
    if score:
        return 'NA score: %s' % score
    else:
        return 'failed.'

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2:
        print na(sys.argv[1])
    else:
        print na()