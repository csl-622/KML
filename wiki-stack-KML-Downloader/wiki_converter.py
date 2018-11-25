#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 11 21:48:53 2018

@author: descentis
"""

import xml.etree.cElementTree as ET
import textwrap
import cgi

'''
This function is used to indent the xml; document is pretty style
'''

instance_id = 1

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

def wiki_file_writer(elem,myFile,prefix):
    global instance_id
    t = '\t'

    Instance = t+t+"<Instance "
    
  
    for ch_elem in elem:             
        if(ch_elem.tag==prefix+'id'):             
            Instance = Instance+ "Id="+'"'+str(instance_id)+'"'+" InstanceType= "+'"'+"wiki/text"+'"'+">\n"
            myFile.write(Instance)
            
            RevisionId = t+t+t+"<RevisionId>"+ch_elem.text+"</RevisionId>\n"
            myFile.write(RevisionId)
            
        if(ch_elem.tag==prefix+'parentid'):
            ParentId = t+t+t+"<ParentId>"+ch_elem.text+"</ParentId>\n" 
            myFile.write(ParentId)
            

            
        
                  
        
        '''
        Timestamp Information
        '''
        if(ch_elem.tag==prefix+'timestamp'):
            '''
            if(f_p!=1):
                Instance = Instance+" InstanceType= "+'"'+"wiki/text"+'"'+">\n"
                myFile.write(Instance)
            '''
            Timestamp = t+t+t+"<TimeStamp>\n"
            myFile.write(Timestamp)
            CreationDate = t+t+t+t+"<CreationDate>"+ch_elem.text+"</CreationDate>\n"
            myFile.write(CreationDate)
            Timestamp = t+t+t+"</TimeStamp>\n"
            myFile.write(Timestamp)            
            
            
        '''
        Contributors information
        '''
        if(ch_elem.tag==prefix+'contributor'):            
            Contributors = t+t+t+"<Contributors>\n"
            myFile.write(Contributors)
            for contrib in ch_elem:
                if(contrib.tag==prefix+'ip'):
                    LastEditorUserName = t+t+t+t+"<LastEditorUserName>"+contrib.text+"</LastEditorUserName>\n"
                    myFile.write(LastEditorUserName)                        
                else:
                    if(contrib.tag==prefix+'username'):
                        LastEditorUserName = t+t+t+t+"<LastEditorUserName>"+contrib.text+"</LastEditorUserName>\n"
                        myFile.write(LastEditorUserName)                        
                    if(contrib.tag==prefix+'id'):
                        LastEditorUserId = t+t+t+t+"<LastEditorUserId>"+contrib.text+"</LastEditorUserId>\n"
                        myFile.write(LastEditorUserId)
                
                    
            Contributors = t+t+t+"</Contributors>\n"
            myFile.write(Contributors)
        
        
        '''
        Body/Text Information
        '''
        if(ch_elem.tag==prefix+'text'):
            Body = t+t+t+"<Body>\n"
            myFile.write(Body)
            text_field = t+t+t+t+"<Text Type="+'"'+"wiki/text"+'"'+" TextSize= "+'"'+ch_elem.attrib['bytes']+'"'+'>\n'
            myFile.write(text_field)
            if(ch_elem.text == None):                
                text_body = "";
            else:
               
                text_body = textwrap.indent(text=ch_elem.text, prefix=t+t+t+t+t)
                text_body = cgi.escape(text_body)
            Body_text = text_body+"\n"
            myFile.write(Body_text)
            text_field = t+t+t+t+"</Text>\n"
            myFile.write(text_field)        
            Body = t+t+t+"</Body>\n"
            myFile.write(Body)            
        
        if(ch_elem.tag==prefix+'comment'):
            Edit = t+t+t+"<EditDetails>\n"
            myFile.write(Edit)
            if(ch_elem.text == None):                
                text_body = "";
            else:
                text_body = textwrap.indent(text=ch_elem.text, prefix=t+t+t+t)
                text_body = cgi.escape(text_body)
            Body_text = text_body+"\n"
            myFile.write(Body_text)
            Edit = t+t+t+"</EditDetails>\n"
            myFile.write(Edit)
        if(ch_elem.tag==prefix+'sha1'):
            sha = t+t+t+"<sha1>"+ch_elem.text+"</sha1>\n"
            myFile.write(sha)

    Instance = t+t+"</Instance>\n"
    myFile.write(Instance)  
    instance_id+=1             

def wiki_kml_converter(name):
    #Creating a meta file for the wiki article
    
    
    
    # To get an iterable for wiki file
    file_name = name+'.xml'
    context_wiki = ET.iterparse(file_name, events=("start","end"))
    # Turning it into an iterator
    context_wiki = iter(context_wiki)
    
    # getting the root element
    event_wiki, root_wiki = next(context_wiki)
    file_name = name+'.kml'
    file_path = name+'/wiki_data/'+file_name
    with open(file_path,"w",encoding='utf-8') as myFile:
        myFile.write("<?xml version='1.0' encoding='utf-8'?>\n")
        myFile.write("<KML>\n") 
        myFile.write("\t<KnowledgeData "+"Type="+'"'+"India"+'"'+">\n")
    prefix = '{http://www.mediawiki.org/xml/export-0.10/}'    #In case of Wikipedia, prefic is required
    for event, elem in context_wiki:
        if event == "end" and elem.tag == prefix+'revision':
     
            with open(file_path,"a",encoding='utf-8') as myFile:
                wiki_file_writer(elem,myFile,prefix)
            
    
    with open(file_path,"a",encoding='utf-8') as myFile:
        myFile.write("\t</KnowledgeData>\n")
        myFile.write("</KML>\n")           
