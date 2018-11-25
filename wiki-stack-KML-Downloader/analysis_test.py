#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 09:39:39 2018

@author: descentis
This program is to test the analysis part of the KML
"""

import xml.etree.cElementTree as ET

# To get an iterable for Comments
meta = ET.iterparse("beer/meta.kml", events=("start","end"))
# Turning it into an iterator
context_meta = iter(meta)

# getting the root element
event_meta, root_meta = next(context_meta)

meta_files = {}     #This is a dictionary which will contain the names of all the meta files present inside the folder

'''
Following code retrieves the file names from meta.kml present inside the folder
'''


for event, elem in context_meta:
    if event == "end" and elem.tag == "Instance":        
        for ch in elem:
            for chi in ch:
                if(elem.attrib['InstanceType']=='posts'):
                    posts_file = chi.attrib['href']
                    meta_files['posts'] = posts_file
                if(elem.attrib['InstanceType']=='posthistory'):
                    posthistory_file = chi.attrib['href']
                    meta_files['posthistory'] = posthistory_file
                if(elem.attrib['InstanceType']=='comments'):
                    comments_file = chi.attrib['href']
                    meta_files['comments'] = comments_file
                if(elem.attrib['InstanceType']=='users'):
                    users_file = chi.attrib['href']
                    meta_files['users'] = users_file
                if(elem.attrib['InstanceType']=='badges'):
                    badges_file = chi.attrib['href']
                    meta_files['badges'] = badges_file
                if(elem.attrib['InstanceType']=='votes'):
                    votes_file = chi.attrib['href']
                    meta_files['votes'] = votes_file


'''
Following code os to retieve the files from the posts folder using 'meta_post.kml'
'''

# To get an iterable for Comments
meta_post = ET.iterparse(posts_file, events=("start","end"))
# Turning it into an iterator
context_post = iter(meta_post)

# getting the root element
event_post, root_post = next(context_post)

for event, elem in context_post:
    if event == "end" and elem.tag == "Instance":
        for ch in elem:
            for chi in ch:
                if(elem.attrib['InstanceType'] == "question_hops"):
                    hops_file = chi.attrib['href']




'''
Following code extracts the 'Score' Value from the posts which are tagged with 'hops'
'''

# To get an iterable for Comments
hops = ET.iterparse(hops_file, events=("start","end"))
# Turning it into an iterator
context_hops = iter(hops)

# getting the root element
event_hops, root_hops = next(context_hops)

for event, elem in context_hops:
    if event == "end" and elem.tag == "Score":
        print(elem.text)