#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 15:05:53 2018

@author: descentis
"""

import xml.etree.cElementTree as ET
import os
import textwrap
import glob
import cgi

count_id = 1
question_id = 1
answer_id = 1
instance_id = 1
post_id = {}
post_history_id = {}
comment_id = {}
votes_id = {}
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



'''
This section contains the list of functions needed for the conversion of post file
'''
def extract_tag(tag):
    tag_list = []
    open_tag = 0
    close_tag = 0
    for i in tag:
        if(i=='>'):
            tag_list.append(tag[open_tag+1:close_tag])
            open_tag=close_tag+1
            close_tag+=1
        else:
            close_tag+=1
    return tag_list

def post_writer(myFile,elem,c,tag_list,post_id,tag_name):
    global question_id
    global answer_id
    t = '\t'
    '''
    For writing the instance field in kml file
    '''
    if(c=="1"):
        Instance = t+t+"<Instance Id= "+'"'+str(post_id[tag_name])+'"'+" "+"InstanceType="+'"'+"question"+'"'
        post_id[tag_name]+=1
    else:
        Instance = t+t+"<Instance Id="+'"'+str(post_id[tag_name])+'"'+" "+"InstanceType="+'"'+"answer"+'"'
        post_id[tag_name]+=1

    Instance = Instance+">\n"
    myFile.write(Instance)    

    '''
    This part is the part of extension mechanism
    '''
    PostId=t+t+t+"<PostId>"+elem.attrib['Id']+"</PostId>\n"
    myFile.write(PostId)
    if(elem.attrib.get("ParentId") != None):
        ParentPostId = t+t+t+"<ParentPostId>"+elem.attrib['ParentId']+"</ParentPostId>"
        myFile.write(ParentPostId)
    if(elem.attrib.get("AcceptedAnswerId") != None):
        AcceptedAnswerId = t+t+t+"<AcceptedAnswerId>"+elem.attrib['AcceptedAnswerId']+"</AcceptedAnswerId>\n"
        myFile.write(AcceptedAnswerId)
    
    '''
    For writing the title in KML
    '''
    if(elem.attrib.get("Title") != None):
        
        Title = t+t+t+"<Title>\n"           
        myFile.write(Title)            
        
        Title_text = t+t+t+'"'+cgi.escape(elem.attrib['Title'])+'"'+"\n"
        myFile.write(Title_text)            
    
        Title = t+t+t+"</Title>\n"           
        myFile.write(Title)                        
    
    
    Tags_element = t+t+t+"<Tags>\n"
    myFile.write(Tags_element)
    for i in tag_list:
        tag = t+t+t+t+"<tag>"+cgi.escape(i)+"</tag>\n"
        myFile.write(tag)
    Tags_element = t+t+t+"</Tags>\n"
    myFile.write(Tags_element)
    
    Reputation_tag = t+t+t+"<Credit> \n"
    myFile.write(Reputation_tag)
    if(elem.attrib.get("Score") != None):
        score = t+t+t+t+"<Score>"+elem.attrib['Score']+"</Score>\n"
        myFile.write(score)
    if(elem.attrib.get("ViewCount") != None):
        ViewCount = t+t+t+t+"<ViewCount>"+elem.attrib['ViewCount']+"</ViewCount>\n"
        myFile.write(ViewCount)
    if(elem.attrib.get("AnswerCount") != None):        
        AnswerCount = t+t+t+t+"<AnswerCount>"+elem.attrib['AnswerCount']+"</AnswerCount>\n"
        myFile.write(AnswerCount)
    if(elem.attrib.get("CommentCount") != None):
        CommentCount = t+t+t+t+"<CommentCount>"+elem.attrib['CommentCount']+"</CommentCount>\n"
        myFile.write(CommentCount)

    if(elem.attrib.get("FavouriteCount") != None):
        FavouriteCount = t+t+t+t+"<FavouriteCount>"+elem.attrib['FavouriteCount']+"</FavouriteCount>\n"
        myFile.write(FavouriteCount)

    Reputation_tag = t+t+t+"</Credit> \n"
    myFile.write(Reputation_tag)
    
    
    TimeStamp = t+t+t+"<TimeStamp>\n"
    myFile.write(TimeStamp)
    if(elem.attrib.get("CreationDate") != None):
        CreationDate = t+t+t+t+"<CreationDate>"+elem.attrib['CreationDate']+"</CreationDate>\n"
        myFile.write(CreationDate)
    if(elem.attrib.get("LastEditDate") != None):
        LastEditDate = t+t+t+t+"<LastEditDate>"+elem.attrib['LastEditDate']+"</LastEditDate>\n"
        myFile.write(LastEditDate)
    if(elem.attrib.get("LastActivityDate") != None):
        LastActivityDate = t+t+t+t+"<LastActivityDate>"+elem.attrib['LastActivityDate']+"</LastActivityDate>\n"
        myFile.write(LastActivityDate)

    if(elem.attrib.get("CommunityOwnedDate") != None):
        CommunityOwnedDate = t+t+t+t+"<CommunityOwnedDate>"+elem.attrib['CommunityOwnedDate']+"</CommunityOwnedDate>\n"
        myFile.write(CommunityOwnedDate)

    if(elem.attrib.get("ClosedDate") != None):
        ClosedDate = t+t+t+t+"<ClosedDate>"+elem.attrib['ClosedDate']+"</ClosedDate>\n"
        myFile.write(ClosedDate)
        
    TimeStamp = t+t+t+"</TimeStamp>\n"
    myFile.write(TimeStamp)
    
    Contributors = t+t+t+"<Contributors>\n"
    myFile.write(Contributors)
    if(elem.attrib.get("OwnerUserId") != None):
        OwnerUserId = t+t+t+t+"<OwnerUserId>"+elem.attrib['OwnerUserId']+"</OwnerUserId>\n"
        myFile.write(OwnerUserId)
    if(elem.attrib.get("LastEditorUserId") != None):
        LastEditorUserId = t+t+t+t+"<LastEditorUserId>"+elem.attrib['LastEditorUserId']+"</LastEditorUserId>\n"
        myFile.write(LastEditorUserId)
    Contributors = t+t+t+"</Contributors>\n"
    myFile.write(Contributors)
    
    Body = t+t+t+"<Body>\n"
    myFile.write(Body)
    text_field = t+t+t+t+"<Text Type="+'"'+"text"+'">\n'
    myFile.write(text_field)
    text_body = textwrap.indent(text=elem.attrib['Body'], prefix=t+t+t+t+t)
    text_body = cgi.escape(text_body)
    Body_text = text_body+"\n"
    myFile.write(Body_text)
    text_field = t+t+t+t+"</Text>\n"
    myFile.write(text_field)        
    Body = t+t+t+"</Body>\n"
    myFile.write(Body)
    Instance = t+t+"</Instance>\n"
    myFile.write(Instance)   


def file_writer(elem, tag_name, c, metaFile, tag_list, name, meta_file_path):
    global count_id
    global post_id
    if(c=="1"):
        file_path = name+'/Posts/Questions/'+tag_name+'.kml'
         
        if(not(os.path.isfile(file_path))):        
            with open(file_path,"w",encoding='utf-8') as myFile:          
                myFile.write("<?xml version='1.0' encoding='utf-8'?>\n")
                myFile.write("<KML>\n")
                myFile.write("\t<KnowledgeData "+"Type="+'"'+"question"+'"'+">\n")
                post_id[tag_name] = 1
                post_writer(myFile,elem,c,tag_list,post_id,tag_name)
            
            t="\t"
            with open(meta_file_path,"a",encoding='utf-8') as metaFile:
                Instance = t+t+"<Instance Id="+'"'+str(count_id)+'"'+" "+"InstanceType="+'"'+"question_"+tag_name+'"'
                Instance = Instance+">\n"
                metaFile.write(Instance)
                id = "k"+str(count_id)
                Kdata = t+t+t+"<KnowledgeData id="+'"'+id+'"'+">\n"
                metaFile.write(Kdata)
                question_include = t+t+t+t+"<xi:include href="+'"'+file_path+'"'+" />\n"
                metaFile.write(question_include)
                Kdata = t+t+t+"</KnowledgeData>\n"
                metaFile.write(Kdata)
                Instance = t+t+"</Instance>\n"
                metaFile.write(Instance)
                count_id+=1
            
    
        else:
            with open(file_path,"a",encoding='utf-8') as myFile:
                post_writer(myFile,elem,c,tag_list,post_id, tag_name)
    
    else:
        file_path = name+'/Posts/Answers/'+tag_name+'.kml'        
        if(not(os.path.isfile(file_path))):        
            with open(file_path,"w",encoding='utf-8') as myFile:          
                myFile.write("<?xml version='1.0' encoding='utf-8'?>\n")
                myFile.write("<KML>\n") 
                myFile.write("\t<KnowledgeData "+"Type="+'"'+"answer"+'"'+">\n")
                post_id[tag_name] = 1
                post_writer(myFile,elem,c,tag_list,post_id,tag_name)

            t="\t"
            with open(meta_file_path,"a",encoding='utf-8') as metaFile:
                Instance = t+t+"<Instance Id="+'"'+str(count_id)+'"'+" "+"InstanceType="+'"'+"answer_"+tag_name+'"'
                Instance = Instance+">\n"
                metaFile.write(Instance)
                id = "k"+str(count_id)
                Kdata = t+t+t+"<KnowledgeData id="+'"'+id+'"'+">\n"
                metaFile.write(Kdata)
                answer_include = t+t+t+t+"<xi:include href="+'"'+file_path+'"'+" />\n"
                metaFile.write(answer_include)    
                Kdata = t+t+t+"</KnowledgeData>\n"
                metaFile.write(Kdata)
                Instance = t+t+"</Instance>\n"
                metaFile.write(Instance)  
                count_id+=1
    
        else:
            with open(file_path,"a",encoding='utf-8') as myFile:
                post_writer(myFile,elem,c,tag_list,post_id,tag_name)
    
        

def KML_creator(context_posts, c, root_posts, Tags, metaFile, name, meta_file_path):
    #post_file_id = 1      # how many number of files you want to create
    
    for event, elem in context_posts:       # elem contains the elements inside the root tag of the XML file i.e. the row in this case
        if event == "end" and elem.tag == "row":          
            
            # This is the processing part                
            
            if(elem.attrib['PostTypeId']==c and c=="1"):
                # PostTypeId=1 means that the post is a question. All the processing here is for the questions.     
                
                tag_list = extract_tag(elem.attrib['Tags'])
                Tags[elem.attrib['Id']] = tag_list
                '''
                for i in tag_list:
                    if(Tags.get(i) == None):
                        count_tags+=1
                        l = []
                        l.append(elem.attrib['Id'])
                        Tags[i] = l
                    else:
                        Tags[i].append(elem.attrib['Id'])            
                '''               
                for i in tag_list:
                    file_writer(elem,i,c,metaFile,tag_list,name,meta_file_path)

                
            
            else:
                if(elem.attrib['PostTypeId']==c and c=="2"):
                    # PostTypeId=2 means that the post is an answer, it is given as c in argument. All the processing here is for the questions.                             
                    
                    if(Tags.get(elem.attrib['ParentId']) != None):
                        tag_list = Tags[elem.attrib['ParentId']]                        
                        for i in tag_list:
                            file_writer(elem,i,c,metaFile,tag_list,name,meta_file_path)  
            elem.clear()
            root_posts.clear()
            
                    
    context_tags = ET.iterparse("Tags.xml", events=("start", "end"))
    context_tags = iter(context_tags)
    event_tags, root_tags = next(context_tags)
    
    for tag_event, tag_elem in context_tags:        
        if tag_event == "end" and tag_elem.tag == "row":
            if(c=="1"):                
                file_path = name+"/Posts/Questions/"+tag_elem.attrib['TagName']+".kml"
                if(os.path.isfile(file_path)):
                    with open(file_path,"a",encoding='utf-8') as myFile:
                        myFile.write("\t</KnowledgeData>\n")
                        myFile.write("</KML>\n")                                        
            else:
                file_path = name+"/Posts/Answers/"+tag_elem.attrib['TagName']+".kml"
                if(os.path.isfile(file_path)):
                    with open(file_path,"a",encoding='utf-8') as myFile:
                        myFile.write("\t</KnowledgeData>\n")
                        myFile.write("</KML>\n")                                                        
                

    


def post_convertor(name):
    
    #Creating the meta file for posts
    meta_file_path = name+"/Posts/meta_posts.kml"             
    
    with open(meta_file_path,"a") as metaFile:
        metaFile.write("<?xml version='1.0' encoding='utf-8'?>\n")
        metaFile.write("<KML>\n") 
        metaFile.write("\t<KnowledgeData "+"Type="+'"'+"meta_posts"+'"'+" xmlns:xi="+'"'+"http://www.w3.org/2001/XInclude"+'"'+">\n")
    
    
    # To get an iterable
    context_posts = ET.iterparse("Posts.xml", events=("start", "end"))
    # turning it into an iterator
    context_posts = iter(context_posts)
    
    # get the root element
    event_posts, root_posts = next(context_posts)
    
    Tags = {}
    KML_creator(context_posts, "1",root_posts, Tags, metaFile, name, meta_file_path)
    # Parsing the Tags so that they can be used in the creation of multiple post files
    '''
    post_tags = ET.parse('Tags.xml')
    root_tags = post_tags.getroot()
    
    # Creating dictionary for tags such that searching is easy
    
    
    Tags = {}
    c = 0
    for i in root_tags:
        Tags[i.attrib['TagName']] = root_tags[c].attrib['Count']
        c=c+1
    root_tags.clear()    
    '''
    
    
    

    # To get an iterable
    context_posts = ET.iterparse("Posts.xml", events=("start", "end"))
    # turning it into an iterator
    context_posts = iter(context_posts)
    
    # get the root element
    event_posts, root_posts = next(context_posts)
    
    KML_creator(context_posts, "2",root_posts, Tags, metaFile, name, meta_file_path)    
    
    with open(meta_file_path,"a",encoding='utf-8') as metaFile:
        metaFile.write("\t</KnowledgeData>\n")
        metaFile.write("</KML>\n")
     
    return Tags



'''
This section contains the list of functions needed for the conversion of post file
''' 

def tag_remover(body):
    for i in body:
        if(i=='<'):
            body = body.replace(i,"")
        if(i=='>'):
            body = body.replace(i,", ")
    return body
  
def history_file_writer(myFile,HistoryType,elem,post_history_id,id):
    global instance_id    
    t = '\t'
    Instance = t+t+"<Instance Id= "+'"'+str(post_history_id[id])+'"'+" "
    post_history_id[id] += 1
    if(elem.attrib.get("PostHistoryTypeId")!=None and int(elem.attrib['PostHistoryTypeId'])<23):
        Instance = Instance+"InstanceType= "+'"'+HistoryType[int(elem.attrib['PostHistoryTypeId'])]+'"'
    else:
        Instance = Instance+'InstanceType= "Unknown"'
    Instance = Instance+" >\n"
    myFile.write(Instance)


    '''
    This is the part of extension mechanism
    '''
    PostId=t+t+t+"<PostId>"+elem.attrib['Id']+"</PostId>\n"
    myFile.write(PostId)
    
    if(elem.attrib.get("PostId") != None):
        ParentPostId = t+t+t+"<ParentPostId>"+elem.attrib['PostId']+"</ParentPostId>\n"
        myFile.write(ParentPostId)        

        
    '''
    For writing the title of instance
    '''
    Title = t+t+t+"<Title>\n"           
    myFile.write(Title)            
    if(elem.attrib.get("PostHistoryTypeId")!=None and int(elem.attrib['PostHistoryTypeId'])<23):
        Title_text = t+t+t+'"'+HistoryType[int(elem.attrib['PostHistoryTypeId'])]+'"'+"\n"
    else:
        Title_text = t+t+t+"Unknown\n"
    myFile.write(Title_text)            

    Title = t+t+t+"</Title>\n"           
    myFile.write(Title)                            

 
    '''
    Timestamp information
    '''

    TimeStamp = t+t+t+"<TimeStamp>\n "
    myFile.write(TimeStamp)
    if(elem.attrib.get("CreationDate") != None):
        CreationDate = t+t+t+t+"<CreationDate>"+elem.attrib['CreationDate']+"</CreationDate> \n"
        myFile.write(CreationDate)
    if(elem.attrib.get("LastEditDate") != None):
        LastEditDate = t+t+t+t+"<LastEditDate>"+elem.attrib['LastEditDate']+"</LastEditDate> \n"
        myFile.write(LastEditDate)
    if(elem.attrib.get("LastActivityDate") != None):
        LastActivityDate = t+t+t+t+"<LastActivityDate>"+elem.attrib['LastActivityDate']+"</LastActivityDate> \n"
        myFile.write(LastActivityDate)
    if(elem.attrib.get("CommunityOwnedDate") != None):
        CommunityOwnedDate = t+t+t+t+"<CommunityOwnedDate>"+elem.attrib['CommunityOwnedDate']+"</CommunityOwnedDate> \n"
        myFile.write(CommunityOwnedDate)
    if(elem.attrib.get("ClosedDate") != None):
        ClosedDate = t+t+t+t+"<ClosedDate>"+elem.attrib['ClosedDate']+"</ClosedDate> \n"
        myFile.write(ClosedDate)
    TimeStamp = t+t+t+"</TimeStamp>\n "
    myFile.write(TimeStamp)
    
 
    '''
    Contributors information
    '''

    Contributors = t+t+t+"<Contributors>\n"
    myFile.write(Contributors)
    if(elem.attrib.get("UserId") != None):
        Contributors =t+t+t+t+"<UserId>"+elem.attrib['UserId']+"</UserId>\n"
        myFile.write(Contributors)
    Contributors = t+t+t+"</Contributors>\n"
    myFile.write(Contributors)

    '''
    PostHistory might have a comment associated with each entry.
    I have added that section as editDetails
    '''
    if(elem.attrib.get('Comment')!=None):        
        Edit = t+t+t+"<EditDetails>\n"
        myFile.write(Edit)
        text_body = textwrap.indent(text=elem.attrib['Comment'], prefix=t+t+t+t)
        text_body = cgi.escape(text_body)
        Body_text = text_body+"\n"
        myFile.write(Body_text)
        Edit = t+t+t+"</EditDetails>\n"
        myFile.write(Edit)        
    
    '''
    Writing the body/text part
    '''
    if(elem.attrib.get('Text')!=None):        
        Body = t+t+t+"<Body>\n"
        myFile.write(Body)
        text_field = t+t+t+t+"<Text Type="+'"'+"text"+'">\n'
        myFile.write(text_field)
        if(elem.attrib['PostHistoryTypeId']=="3" or elem.attrib['PostHistoryTypeId']=="6"):            
            body_text = elem.attrib['Text']
            body_text = tag_remover(body_text)
            text_body = textwrap.indent(text=body_text, prefix=t+t+t+t+t)
            text_body = cgi.escape(text_body)
        else:
            text_body = textwrap.indent(text=elem.attrib['Text'], prefix=t+t+t+t+t)
            text_body = cgi.escape(text_body)
        Body_text = text_body+"\n"
        myFile.write(Body_text)
        text_field = t+t+t+t+"</Text>\n"
        myFile.write(text_field)        
        Body = t+t+t+"</Body>\n"
        myFile.write(Body)
    

    Instance = t+t+"</Instance>\n"
    myFile.write(Instance)       
    

def post_history_convertor(name, Tags):
    global post_history_id
    # Creating the meta file for post_history
    meta_file_path = name+"/Posthistory/meta_posthistory.kml"             
    with open(meta_file_path,"a") as metaFile:
        metaFile.write("<?xml version='1.0' encoding='utf-8'?>\n")
        metaFile.write("<KML>\n") 
        metaFile.write("\t<KnowledgeData "+"Type="+'"'+"meta_posthistory"+'"'+" xmlns:xi="+'"'+"http://www.w3.org/2001/XInclude"+'"'+">\n")   
        
    # To get an iterable for posthistory
    context_posthistory = ET.iterparse("PostHistory.xml", events=("start","end"))
    # Turning it into an iterator
    context_posthistory = iter(context_posthistory)
    
    # getting the root element
    event_posthistory, root_posthistory = next(context_posthistory)
    
    # Dictionary of postHistoryType
    HistoryType = {1:'Initial Title',2:'Initial Body',3:'Initial Tags',4:'Edit Title',5:'Edit Body',6:'Edit Tags',7:'Rollback Title',8:'Rollback Body',
                   9:'Rollback Tags',10:'Post Closed',11:'Post Reopened',12:'Post Deleted',13:'Post Undeleted',14:'Post Locked',15:'Post Unlocked',
                   16:'Community Owned',17:'Post Migrated',18:'Question Merged',19:'Question Protected',20:'Question Unprotected',21:'Post Disassociated',
                   22:'Question Unmerged'}
    c_id = 1
    t = '\t'
    global instance_id
    instance_id = 1
    for event, elem in context_posthistory:
        if event == "end" and elem.tag == "row":
            post_id = elem.attrib['PostId']
            if(Tags.get(post_id)!=None):
                f_list = Tags[post_id]
                for id in f_list:
                    file_path = name+'/Posthistory/'+id+'.kml'
                    if(not(os.path.isfile(file_path))):
                        with open(file_path,"w",encoding='utf-8') as myFile:
                            myFile.write("<?xml version='1.0' encoding='utf-8'?>\n")
                            myFile.write("<KML>\n") 
                            myFile.write("\t<KnowledgeData "+"Type="+'"'+"posthistory"+'"'+">\n")
                            post_history_id[id] = 1
                            history_file_writer(myFile,HistoryType,elem,post_history_id,id)
                        with open(meta_file_path,"a",encoding='utf-8') as metaFile:                        
                            Instance = t+t+"<Instance Id="+'"'+str(c_id)+'"'+" "+"InstanceType="+'"'+id+'"'
                            Instance = Instance+">\n"
                            metaFile.write(Instance)
                            id = "k"+str(c_id)
                            Kdata = t+t+t+"<KnowledgeData id="+'"'+id+'"'+">\n"
                            metaFile.write(Kdata)
                            post_include = t+t+t+t+"<xi:include href="+'"'+file_path+'"'+" />\n"
                            metaFile.write(post_include)
                            Kdata = t+t+t+"</KnowledgeData>\n"
                            metaFile.write(Kdata)
                            Instance = t+t+"</Instance>\n"
                            metaFile.write(Instance)
                            c_id+=1
    
                        
                    else:
                        with open(file_path,"a",encoding='utf-8') as myFile:
                            history_file_writer(myFile,HistoryType,elem,post_history_id,id)
            
            elem.clear()
            root_posthistory.clear()
    
    file_list = glob.glob(name+"/Posthistory/*.kml")
    for file_path in file_list:
        if(os.path.isfile(file_path)):
            with open(file_path,"a",encoding='utf-8') as myFile:
                myFile.write("\t</KnowledgeData>\n")
                myFile.write("</KML>\n")           




'''
This is the comment section
'''

def comment_file_writer(myFile,elem,comment_id,id):
    
    
    t = '\t'    
    Instance = t+t+"<Instance Id="+'"'+str(comment_id[id])+'"'+" "
    comment_id[id]+=1
    Instance = Instance+" InstanceType= "+'"'+"comments"+'"'

    if(elem.attrib.get("Score") != None):
        Instance = Instance+" "+"Score="+'"'+elem.attrib['Score']+'"'
    

    
    Instance = Instance+">\n"
    myFile.write(Instance)    

    '''
    This is the part of extension mechanism
    '''
    PostId = t+t+t+"<PostId>"+elem.attrib['Id']+"</PostId>\n"
    myFile.write(PostId)
    
    if(elem.attrib.get("PostId") != None):
        ParentPostId = t+t+t+"<ParentPostId>"+elem.attrib['PostId']+"</ParentPostId>\n"
        myFile.write(ParentPostId)

    '''
    Contributors information
    '''

    Contributors = t+t+t+"<Contributors>\n"
    myFile.write(Contributors)
    if(elem.attrib.get("UserId") != None):
        Contributors = t+t+t+t+"<UserId>"+elem.attrib['UserId']+"</UserId>\n"
        myFile.write(Contributors)
    Contributors = t+t+t+"</Contributors>\n"
    myFile.write(Contributors)


    '''
    Timestamp information
    '''

    TimeStamp = t+t+t+"<TimeStamp>\n"
    myFile.write(TimeStamp)
    if(elem.attrib.get("CreationDate") != None):        
        CreationDate = t+t+t+t+"<CreationDate>"+elem.attrib['CreationDate']+"</CreationDate>\n"
        myFile.write(CreationDate)
    if(elem.attrib.get("LastEditDate") != None):
        LastEditDate = t+t+t+t+"<LastEditDate>"+elem.attrib['LastEditDate']+"</LastEditDate>\n"
        myFile.write(LastEditDate)
    if(elem.attrib.get("LastActivityDate") != None):
        LastActivityDate = t+t+t+t+"<LastActivityDate>"+elem.attrib['LastActivityDate']+"</LastActivityDate>\n"
        myFile.write(LastActivityDate)     
    if(elem.attrib.get("CommunityOwnedDate") != None):
        CommunityOwnedDate = t+t+t+t+"<CommunityOwnedDate>"+elem.attrib['CommunityOwnedDate']+"</CommunityOwnedDate>\n"
        myFile.write(CommunityOwnedDate)
    if(elem.attrib.get("ClosedDate") != None):
        ClosedDate = t+t+t+t+"<ClosedDate>"+elem.attrib['ClosedDate']+"</ClosedDate>\n"
        myFile.write(ClosedDate)
    TimeStamp = t+t+t+"</TimeStamp>\n"
    myFile.write(TimeStamp)


    '''
    Writing the body/text part
    '''
    if(elem.attrib.get('Text')!=None):        
        Body = t+t+t+"<Body>\n"
        myFile.write(Body)
        text_field = t+t+t+t+"<Text Type="+'"'+"text"+'">\n'
        myFile.write(text_field)
        text_body = textwrap.indent(text=elem.attrib['Text'], prefix=t+t+t+t+t)
        text_body = cgi.escape(text_body)
        Body_text = text_body+"\n"
        myFile.write(Body_text)
        text_field = t+t+t+t+"</Text>\n"
        myFile.write(text_field)        
        Body = t+t+t+"</Body>\n"
        myFile.write(Body)

    Instance = t+t+"</Instance>\n"
    myFile.write(Instance)       


def comments_converter(name, Tags):
    
    global comment_id
    #Creating the meta file for Comments
    meta_file_path = name+"/Comments/meta_comments.kml"             
    with open(meta_file_path,"a",encoding='utf-8') as metaFile:
        metaFile.write("<?xml version='1.0' encoding='utf-8'?>\n")
        metaFile.write("<KML>\n") 
        metaFile.write("\t<KnowledgeData "+"Type="+'"'+"meta_comments"+'"'+" xmlns:xi="+'"'+"http://www.w3.org/2001/XInclude"+'"'+">\n")
    
    # To get an iterable for Comments
    context_comments = ET.iterparse("Comments.xml", events=("start","end"))
    # Turning it into an iterator
    context_comments = iter(context_comments)
    
    # getting the root element
    event_comments, root_comments = next(context_comments)
    
    c_id = 1
    global instance_id
    instance_id+=1
    t='\t'
    for event, elem in context_comments:
        if event == "end" and elem.tag == "row":            
            post_id = elem.attrib['PostId']
            if(Tags.get(post_id)!=None):
                f_list = Tags[post_id]
            for id in f_list:
                file_path = name+'/Comments/'+id+'.kml'
                if(not(os.path.isfile(file_path))):
                    with open(file_path,"w",encoding='utf-8') as myFile:
                        myFile.write("<?xml version='1.0' encoding='utf-8'?>\n")
                        myFile.write("<KML>\n") 
                        myFile.write("\t<KnowledgeData "+"Type="+'"'+"comments"+'"'+">\n")
                        comment_id[id] = 1
                        comment_file_writer(myFile,elem,comment_id,id)
                        
                    with open(meta_file_path,"a",encoding='utf-8') as metaFile:                        
                        Instance = t+t+"<Instance Id="+'"'+str(c_id)+'"'+" "+"InstanceType="+'"'+id+'"'
                        Instance = Instance+">\n"
                        metaFile.write(Instance)
                        id = "k"+str(c_id)
                        Kdata = t+t+t+"<KnowledgeData id="+'"'+id+'"'+">\n"
                        metaFile.write(Kdata)
                        post_include = t+t+t+t+"<xi:include href="+'"'+file_path+'"'+" />\n"
                        metaFile.write(post_include)
                        Kdata = t+t+t+"</KnowledgeData>\n"
                        metaFile.write(Kdata)
                        Instance = t+t+"</Instance>\n"
                        metaFile.write(Instance)
                        c_id+=1                        
                        
                else:
                    with open(file_path,"a",encoding='utf-8') as myFile:
                        comment_file_writer(myFile,elem,comment_id,id)
                
            elem.clear()
            root_comments.clear()       

    file_list = glob.glob(name+"/Comments/*.kml")
    for file_path in file_list:
        if(os.path.isfile(file_path)):
            with open(file_path,"a",encoding='utf-8') as myFile:
                myFile.write("\t</KnowledgeData>\n")
                myFile.write("</KML>\n")           




'''
Users section
'''

def users_file_writer(myFile,elem):
    global instance_id
    t = '\t'    
    Instance = t+t+"<Instance Id="+'"'+elem.attrib['Id']+'"'+" "
    if(elem.attrib.get("PostId") != None):
        Instance = Instance+" "+"ParentId="+'"'+elem.attrib['PostId']+'"'
    
    Instance = Instance+" InstanceType= "+'"'+"users"+'"'

    Instance = Instance+">\n"
    myFile.write(Instance)    


    '''
    Timestamp information
    '''

    TimeStamp = t+t+t+"<TimeStamp>\n"
    myFile.write(TimeStamp)
    if(elem.attrib.get("CreationDate") != None):
        CreationDate = t+t+t+t+"<CreationDate>"+elem.attrib['CreationDate']+"</CreationDate> \n"
        myFile.write(CreationDate)
    if(elem.attrib.get("LastEditDate") != None):
        LastEditDate = t+t+t+t+"<LastEditDate>"+elem.attrib['LastEditDate']+"</LastEditDate> \n"
        myFile.write(LastEditDate)        
    if(elem.attrib.get("LastAccessDate") != None):
        LastAccessDate = t+t+t+t+"<LastAccessDate>"+elem.attrib['LastAccessDate']+"</LastAccessDate> \n"
        myFile.write(LastAccessDate)        
    if(elem.attrib.get("CommunityOwnedDate") != None):
        CommunityOwnedDate = t+t+t+t+"<CommunityOwnedDate>"+elem.attrib['CommunityOwnedDate']+"</CommunityOwnedDate> \n"
        myFile.write(CommunityOwnedDate)        
    if(elem.attrib.get("ClosedDate") != None):
        ClosedDate = t+t+t+t+"<ClosedDate>"+elem.attrib['ClosedDate']+"</ClosedDate> \n"
        myFile.write(ClosedDate)        
    TimeStamp = t+t+t+"</TimeStamp>\n"
    myFile.write(TimeStamp)


    '''
    Reputation Information (Renamed as Credit)
    '''
    Reputation_tag = t+t+t+"<Credit>\n"
    myFile.write(Reputation_tag)
    if(elem.attrib.get("Score") != None):
        Reputation = t+t+t+t+"<Score>"+elem.attrib['Score']+"</Score> \n"
        myFile.write(Reputation)
    if(elem.attrib.get("Views") != None):
        ViewCount = t+t+t+t+"<ViewCount>"+elem.attrib['Views']+"</ViewCount> \n"
        myFile.write(ViewCount)
    if(elem.attrib.get("UpVotes") != None):        
        UpVotes = t+t+t+t+"<UpVotes>"+elem.attrib['UpVotes']+"</UpVotes> \n"
        myFile.write(UpVotes)
    if(elem.attrib.get("DownVotes") != None):
        DownVotes = t+t+t+t+"<DownVotes>"+elem.attrib['DownVotes']+"</DownVotes> \n"
        myFile.write(DownVotes)
    if(elem.attrib.get("FavouriteCount") != None):
        FavouriteCount = t+t+t+t+"<FavouriteCount>"+elem.attrib['FavouriteCount']+"</FavouriteCount> \n"
        myFile.write(FavouriteCount)
    
    Reputation_tag = t+t+t+"</Credit>\n"
    myFile.write(Reputation_tag)

    '''
    Contributors Details
    '''
    Contributors = t+t+t+"<Contributors>\n"
    myFile.write(Contributors)
    if(elem.attrib.get("Id") != None):
        Contributors = t+t+t+t+"<UserId>"+elem.attrib['Id']+"</UserId>\n"
        myFile.write(Contributors)
    if(elem.attrib.get("DisplayName") != None):
        display_name = t+t+t+t+"<DisplayName>"+cgi.escape(elem.attrib['DisplayName'])+"</DisplayName>\n"
        myFile.write(display_name)
    if(elem.attrib.get("EmailHash") != None):
        email = t+t+t+t+"<Email>"+cgi.escape(elem.attrib['EmailHash'])+"</Email>\n"
        myFile.write(email)
    if(elem.attrib.get("WebsiteUrl") != None):
        web = t+t+t+t+"<Website>"+cgi.escape(elem.attrib['WebsiteUrl'])+"</Website>\n"
        myFile.write(web)
    if(elem.attrib.get("Location") != None):
        location = t+t+t+t+"<Location>"+cgi.escape(elem.attrib['Location'])+"</Location>\n"
        myFile.write(location)
    if(elem.attrib.get("Age") != None):
        age = t+t+t+t+"<Age>"+cgi.escape(elem.attrib['Age'])+"</Age>\n"
        myFile.write(age)
    Contributors = t+t+t+"</Contributors>\n"
    myFile.write(Contributors)    

    '''
    Writing the body/text part
    '''
    Body = t+t+t+"<Body>\n"
    myFile.write(Body)
    
    if(elem.attrib.get('AboutMe')!=None):
        text_field = t+t+t+t+"<Text Type="+'"'+"about"+'">\n'
        myFile.write(text_field)
        text_body = textwrap.indent(text=elem.attrib['AboutMe'], prefix=t+t+t+t+t)
        text_body = cgi.escape(text_body)
        Body_text = text_body+"\n"
        myFile.write(Body_text)    
        text_field = t+t+t+t+"</Text>\n"
        myFile.write(text_field)        
        
    Body = t+t+t+"</Body>\n"
    myFile.write(Body)    
    Instance = t+t+"</Instance>\n"
    myFile.write(Instance)          


def user_converter(name):
    #creating the meta file
    
    # To get an iterable for Comments
    context_users = ET.iterparse("Users.xml", events=("start","end"))
    # Turning it into an iterator
    context_users = iter(context_users)
    
    # getting the root element
    event_users, root_users = next(context_users)

    file_path = name+'/Users/users.kml'
    with open(file_path,"a",encoding='utf-8') as myFile:
        myFile.write("<?xml version='1.0' encoding='utf-8'?>\n")
        myFile.write("<KML>\n") 
        myFile.write("\t<KnowledgeData "+"Type="+'"'+"Users"+'"'+">\n")
    for event, elem in context_users:
        if event == "end" and elem.tag == "row":            
            with open(file_path,"a",encoding='utf-8') as myFile:
                users_file_writer(myFile,elem)            
            
            elem.clear()
            root_users.clear()
            
    file_path = name+'/Users/users.kml'    
    with open(file_path,"a",encoding='utf-8') as myFile:
        myFile.write("\t</KnowledgeData>\n")
        myFile.write("</KML>\n")               


'''
Votes Section
'''
instance_id = 1
def voters_file_writer(myFile, elem, vote_type, id_list):
    t = '\t'    
  
    Instance = t+t+"<Instance Id="+'"'+str(id_list[elem.attrib['PostId']])+'"'+" "
    
    '''
    This code was to include the parent Id, since the parent ID is already included in the file name and hence is not required.
    if(elem.attrib.get("PostId") != None):
        Instance = Instance+" "+"ParentId="+'"'+elem.attrib['PostId']+'"'
    '''
    
    if(vote_type.get(elem.attrib['VoteTypeId'])!=None):
        Instance = Instance+" InstanceType= "+'"'+vote_type[elem.attrib['VoteTypeId']]+'"'
    else:
        Instance = Instance+" InstanceType= "+'"'+"unknown"+'"'

    Instance = Instance+">\n"
    myFile.write(Instance)


    '''
    Timestamp information
    '''

    TimeStamp = t+t+t+"<TimeStamp>\n"
    myFile.write(TimeStamp)
    if(elem.attrib.get("CreationDate") != None):
        CreationDate = t+t+t+t+"<CreationDate>"+elem.attrib['CreationDate']+"</CreationDate>\n"
        myFile.write(CreationDate)
    TimeStamp = t+t+t+"</TimeStamp>\n"
    myFile.write(TimeStamp)    
    

    '''
    Reputation Information
    '''

    if(elem.attrib.get("BountyAmount") != None):
        Reputation_tag = t+t+t+"<Credit>\n"
        myFile.write(Reputation_tag)
        BountyAmount = t+t+t+t+"<BountyAmount>"+elem.attrib['BountyAmount']+"</BountyAmount>\n"
        myFile.write(BountyAmount)
        Reputation_tag = t+t+t+"</Credit>\n"    
        myFile.write(Reputation_tag)



    '''
    Contributors information
    '''


    if(elem.attrib.get("UserId") != None):
        Contributors = t+t+t+"<Contributors>\n"
        myFile.write(Contributors)
        UserId = t+t+t+t+"<UserId>"+elem.attrib['UserId']+"</UserId>\n"
        myFile.write(UserId)
        Contributors = t+t+t+"</Contributors>\n"
        myFile.write(Contributors)    

    Instance = t+t+"</Instance>\n"
    myFile.write(Instance)          


def votes_converter(name):

    #Creating the meata file    
    meta_file_path = name+"/Votes/meta_votes.kml"             
    with open(meta_file_path,"a") as metaFile:
        metaFile.write("<?xml version='1.0' encoding='utf-8'?>\n")
        metaFile.write("<KML>\n") 
        metaFile.write("\t<KnowledgeData "+"Type="+'"'+"meta_votes"+'"'+" xmlns:xi="+'"'+"http://www.w3.org/2001/XInclude"+'"'+">\n")    
    
    # To get an iterable for Votes
    context_votes = ET.iterparse("Votes.xml", events=("start","end"))
    # Turning it into an iterable
    context_votes = iter(context_votes)
    
    #Getting the root element
    event_votes,root_votes = next(context_votes)

    vote_type = {'1':'AcceptedByOriginator','2':'UpMod','3':'DownMod','4':'Offensive','5':'Favorite','6': 'Close','7': 'Reopen','8': 'BountyStart','9': 'BountyClose','10': 'Deletion','11': 'Undeletion','12': 'Spam','13': 'InformModerator'}    
    post_id = {}
    c_id = 1
    t = '\t'
    
    '''
    Creating instance ID list for voters
    '''
    id_list = {}
    
    for event, elem in context_votes:
        if event == "end" and elem.tag == "row":
            if(post_id.get(elem.attrib['PostId'])==None):
                post_id[elem.attrib['PostId']] = elem.attrib['PostId']
                id_list[elem.attrib['PostId']] = 1
                file_path = name+'/Votes/PostId_'+elem.attrib['PostId']+'.kml'
                with open(file_path,"w",encoding='utf-8') as myFile:
                    myFile.write("<?xml version='1.0' encoding='utf-8'?>\n")
                    myFile.write("<KML>\n") 
                    myFile.write("\t<KnowledgeData "+"Type="+'"'+"Votes"+'"'+">\n")
                    voters_file_writer(myFile,elem,vote_type,id_list)
                id_list[elem.attrib['PostId']] += 1
                    
                with open(meta_file_path,"a",encoding='utf-8') as metaFile:                        
                    Instance = t+t+"<Instance Id="+'"'+str(c_id)+'"'+" "+"InstanceType="+'"'+'PostId_'+elem.attrib['PostId']+'"'
                    Instance = Instance+">\n"
                    metaFile.write(Instance)
                    id = "k"+str(c_id)
                    Kdata = t+t+t+"<KnowledgeData id="+'"'+id+'"'+">\n"
                    metaFile.write(Kdata)
                    post_include = t+t+t+t+"<xi:include href="+'"'+file_path+'"'+" />\n"
                    metaFile.write(post_include)
                    Kdata = t+t+t+"</KnowledgeData>\n"
                    metaFile.write(Kdata)
                    Instance = t+t+"</Instance>\n"
                    metaFile.write(Instance)
                    c_id+=1                                            
                    

            else:
                file_path = name+'/Votes/PostId_'+elem.attrib['PostId']+'.kml'
                with open(file_path,"a",encoding='utf-8') as myFile:
                    voters_file_writer(myFile,elem,vote_type, id_list)
                id_list[elem.attrib['PostId']] += 1
            
            elem.clear()
            root_votes.clear()
    
    file_list = glob.glob(name+"/Votes/*.kml")
    for file_path in file_list:
        if(os.path.isfile(file_path)):
            with open(file_path,"a",encoding='utf-8') as myFile:
                myFile.write("\t</KnowledgeData>\n")
                myFile.write("</KML>\n")               


'''
Badges section
'''

def badges_file_writer(myFile, elem):
    t = '\t'    
    Instance = t+t+"<Instance Id="+'"'+elem.attrib['Id']+'"'+" "
    if(elem.attrib.get("UserId") != None):
        Instance = Instance+" "+"UserId="+'"'+elem.attrib['UserId']+'"'    
    
    Instance = Instance+" InstanceType= "+'"'+"badges"+'"'
    Instance = Instance+">\n"
    myFile.write(Instance) 

 
    '''
    For writing the title of instance
    '''
    Title = t+t+t+"<Title>\n"           
    myFile.write(Title)            
    if(elem.attrib.get("Name")!=None):
        Title_text = t+t+t+'"'+elem.attrib['Name']+'"'+"\n"
        Title_text = cgi.escape(Title_text)
    myFile.write(Title_text)            

    Title = t+t+t+"</Title>\n"           
    myFile.write(Title)                       


    '''
    Timestamp information
    '''

    TimeStamp = t+t+t+"<TimeStamp>\n"
    myFile.write(TimeStamp)
    if(elem.attrib.get("Date") != None):
        Date = t+t+t+t+"<Date>"+elem.attrib['Date']+"</Date>\n"
        myFile.write(Date)
    TimeStamp = t+t+t+"</TimeStamp>\n"
    myFile.write(TimeStamp)    

    Instance = t+t+"</Instance>\n"
    myFile.write(Instance)          


def badges_converter(name):
    # Creating the meta file
    
    
    
    # To get an iterable for Votes
    context_badges = ET.iterparse("Badges.xml", events=("start","end"))
    # Turning it into an iterable
    context_badges = iter(context_badges)
    
    #Getting the root element
    event_badges,root_badges = next(context_badges)    

    user_id = {}
    
    for event, elem in context_badges:
        if event == "end" and elem.tag == "row":
            if(user_id.get(elem.attrib['UserId'])==None):
                user_id[elem.attrib['UserId']] = elem.attrib['UserId']
                file_path = name+'/Badges/UserId_'+elem.attrib['UserId']+'.kml'
                with open(file_path,"w",encoding='utf-8') as myFile:
                    myFile.write("<?xml version='1.0' encoding='utf-8'?>\n")
                    myFile.write("<KML>\n") 
                    myFile.write("\t<KnowledgeData "+"Type="+'"'+"Badges"+'"'+">\n")
                    badges_file_writer(myFile,elem)                

            else:
                file_path = name+'/Badges/UserId_'+elem.attrib['UserId']+'.kml'
                with open(file_path,"a",encoding='utf-8') as myFile:
                    badges_file_writer(myFile,elem)
                    
                    
            elem.clear()
            root_badges.clear()
            
            
    file_list = glob.glob(name+"/Badges/*.kml")
    for file_path in file_list:
        if(os.path.isfile(file_path)):
            with open(file_path,"a",encoding='utf-8') as myFile:
                myFile.write("\t</KnowledgeData>\n")
                myFile.write("</KML>\n")               