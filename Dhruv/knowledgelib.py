#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 14:31:51 2018

@author: descentis
"""

from meta_file import meta_maker
from create_directory import make_path
from post_conversion import post_convertor
from post_conversion import post_history_convertor
from post_conversion import comments_converter
from post_conversion import user_converter
from post_conversion import votes_converter
from post_conversion import badges_converter
from internetarchive import download
from download_wiki import get_wiki_byname
from wiki_converter import wiki_kml_converter
from subprocess import call
import os


def SE_converter(name):
    # Creating a directory for KML data
    make_path(name+"/Posts/Questions")
    make_path(name+"/Posts/Answers")
    make_path(name+"/Comments")
    make_path(name+"/Users")
    make_path(name+"/Badges")
    make_path(name+"/Posthistory")
    make_path(name+"/Votes")
    # First creating the meta file for StackExchange dumps
    meta_maker(name)
    
    Tags = post_convertor(name)
    
    post_history_convertor(name,Tags)
    
    comments_converter(name, Tags)
    
    user_converter(name)
    
    votes_converter(name)
    
    badges_converter(name)


'''
This part of the program downloads the stack exchange data
'''

def stack_downloader(name):
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
    call(["7z","x",'stackexchange/'+site_name[name]])
    
    '''
    calling the KML converter for Stack_exchange
    '''
    SE_converter(name)
    dir_name = os.getcwd()
    file_list = os.listdir(dir_name)
    for file in file_list:
        if (file.endswith(".xml")):
            os.remove(os.path.join(dir_name, file))
    
def wiki_converter(name):
    #creating path for wiki kml data
    make_path(name+"/wiki_data")
    wiki_list = []
    wiki_list.append(name)
    get_wiki_byname(wiki_list)
    wiki_kml_converter(name)