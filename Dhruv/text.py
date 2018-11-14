#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 07:42:38 2018

@author: descentis
"""
from internetarchive import download
from subprocess import call

name = "3dprinting"
name = name.lower()
stack_exchange_list = []
name_list = []
f = open("site_list.txt","r")
while True:
    a = f.readline()
    a = a[:len(a)-1]
    stack_exchange_list.append(a)
    l = []
    for i in a:
        if(i=='.'):
            break
        l.append(i)
    x = ''.join(l)
    name_list.append(x)
    if(not f.readline()):
        break
del name_list[len(name_list)-1]
site_name = {}
for i in range(len(name_list)):
    site_name[name_list[i]] = stack_exchange_list[i]

download('stackexchange', verbose=True, glob_pattern=site_name[name])
call(["7z","x",site_name[name]])