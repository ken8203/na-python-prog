#! /usr/bin/env python
# -*-coding: utf-8 -*-
# file: na_subprocess_check_ouput.py

import subprocess

output = subprocess.check_output(['ls', '-al'])
print output

'''
total 4148360
drwxr-xr-x+ 36 jaychung  staff        1224  2 22 13:55 .
drwxr-xr-x+ 81 jaychung  staff        2754  2 22 21:54 ..
-rwxr-xr-x@  1 jaychung  staff        8196  2  1 15:39 .DS_Store
-rwxr-xr-x   1 jaychung  staff           0  2  7  2015 .localized
-rw-r-----@  1 jaychung  staff     1517152 12 11 12:42 416308.pdf
-rw-r-----@  1 jaychung  staff     4173323 11  5 21:14 OReilly.Web.Scraping.with.Python.2015.6.pdf
-rw-r-----@  1 jaychung  staff      896727 12 23 10:41 WWW簡介.pdf
drwxr-xr-x  18 jaychung  staff         612  1 19 21:38 api
drwxr-xr-x  11 jaychung  staff         374  2 19 20:32 cscc
-rw-r--r--@  1 jaychung  staff      296703 11 25 12:39 dooooor.pdf
-rw-r--r--@  1 jaychung  staff       28893 12 21 17:55 fb.jpg
drwxr-xr-x@ 11 jaychung  staff         374 11 10 15:23 garand-sticky-1643193
-rw-r--r--@  1 jaychung  staff      396752 12 23 10:16 msdn.key
-rw-r-----@  1 jaychung  staff      234165  7 13  2015 multigon_3d_wallpaper_by_momkay-wallpaper-1440x900.jpg
-rw-r--r--   1 jaychung  staff         170  2 22 21:54 na_os_path.py
-rw-r--r--@  1 jaychung  staff      793579  2 19 21:55 na_python_prog.key
drwx------@  6 jaychung  staff         204 12 23 16:48 neon-bootstrap-admin-theme
drwxr-xr-x  27 jaychung  staff         918  1  7 14:49 recommender-letter
-rw-r-----@  1 jaychung  staff     4392933 11 18 10:56 shutterstock_219087994.jpg
drwxr-xr-x@ 13 jaychung  staff         442  9 15 06:23 smooth-scroll-master
drwxr-xr-x   7 jaychung  staff         238  1  4 16:23 temp
drwxr-xr-x  18 jaychung  staff         612  2 12 01:23 urlfit
-rw-------@  1 jaychung  staff         165  1 13 23:33 ~$Hw6_LDAP Puppet Jail.pptx
-rw-------@  1 jaychung  staff         162 10 31 01:52 ~$PP-Homework-1.docx
-rw-------@  1 jaychung  staff         171 11 24 20:48 ~$unique_count_ingredients.xlsx
-rw-r--r--@  1 jaychung  staff      283498 12 20 21:52 螢幕快照 2015-12-20 下午9.52.28.png
-rw-r--r--@  1 jaychung  staff      288724 12 20 21:52 螢幕快照 2015-12-20 下午9.52.42.png
-rw-r--r--@  1 jaychung  staff      158020  1 31 19:31 螢幕快照 2016-01-31 下午7.31.40.png
-rw-r--r--@  1 jaychung  staff      157932  1 31 19:33 螢幕快照 2016-01-31 下午7.33.33.png
-rw-r--r--@  1 jaychung  staff       97399  2  3 19:07 螢幕快照 2016-02-03 下午7.07.41.png
-rw-r--r--@  1 jaychung  staff      123172  2  3 19:13 螢幕快照 2016-02-03 下午7.13.23.png
-rw-r--r--@  1 jaychung  staff     1640994  2  4 20:42 螢幕快照 2016-02-04 下午8.42.35.png
-rw-r--r--@  1 jaychung  staff      665149  2 19 23:19 螢幕快照 2016-02-19 下午11.19.38.png
-rw-r--r--@  1 jaychung  staff       94652  2 19 00:41 螢幕快照 2016-02-19 上午12.41.21.png
-rw-r--r--@  1 jaychung  staff  2039989033  2 20 13:52 万万没想到.Surprise.2015.HD1080P.X264.AAC.mp4
-rw-r-----@  1 jaychung  staff    67658436 11  5 21:07 基于开源工具的数据分析.pdf
'''