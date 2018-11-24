#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 10:42:44 2018

@author: descentis
"""

import xml.etree.cElementTree as ET
import sys
# KML is the root tag

def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def meta_maker(name):
    KML = ET.Element('KML')
    '''
    Key = ET.SubElement(KML, "Key")
    Key.set("attr.name","posts")
    Key.set("attr.type","string")
    Key.set("for","KnowledgeData")
    Key.set("id","posts")
    '''
    
    org_stdout = sys.stdout
    KnowledgeData = ET.SubElement(KML,"KnowledgeData")
    KnowledgeData.set("Type","meta")
    path_name = {0:name+"/Posts/meta_posts.kml",1:name+"/Posthistory/meta_post_history.kml",2:name+"/Comments/meta_comments.kml",3:name+"/Users/meta_users.kml",4:name+"/Badges/badges.kml",5:name+"/Votes/meta_votes.kml"}
    instance_type = ["posts","posthistory","comments","users","badges","votes"]
    for i in range(6):
        Instance = ET.SubElement(KnowledgeData,"Instance")
        Instance.set("Id",str(i+1))
        Instance.set("InstanceType",instance_type[i])
        Instance.set("xmlns:xi","http://www.w3.org/2001/XInclude")
        Kdata = ET.SubElement(Instance,"KnowledgeData")
        id = "k"+str(i+1)
        Kdata.set("Id",id)
        x_include = ET.SubElement(Kdata,"xi:include")
        x_include.set("href",path_name[i])
 
    
    tree = ET.ElementTree(KML)
    
    indent(KML)
    file_name = name+'/'+'meta.kml'
    f = open(file_name,'wb')
    sys.stdout = f
    tree.write(sys.stdout,encoding="utf-8-sig")
    f.close()
    sys.stdout = org_stdout