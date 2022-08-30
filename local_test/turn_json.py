#!/usr/bin/python
# -*- coding:utf8 -*-
with open ( 'a.json', 'r' ) as f1, open ( 'Kaoyan.json', 'a+' ) as f2:
    f2.writelines ( '[' )
    for line in f1:
        f2.writelines ( line + ',' )
    f2.writelines ( ']' )
