import xml.etree.cElementTree as ec
import numpy as np
import os
import matplotlib.pyplot as plt
from nltk.tag import pos_tag

path = "/home/paras/KML/resources/Indian Institute of Technology Ropar.xml"
path2 = "/home/paras/KML/compressed-KML/compressedIIT.kml"

XML_article_len = []
KML_article_len = []

def cleanString(incomingString):
    newstring = incomingString
    newstring = newstring.replace("!","")
    newstring = newstring.replace("@","")
    newstring = newstring.replace("#","")
    newstring = newstring.replace("$","")
    newstring = newstring.replace("%","")
    newstring = newstring.replace("^","")
    newstring = newstring.replace("&","")
    newstring = newstring.replace("*","")
    newstring = newstring.replace("(","")
    newstring = newstring.replace(")","")
    newstring = newstring.replace("+","")
    newstring = newstring.replace("=","")
    newstring = newstring.replace("?","")
    newstring = newstring.replace("\'","")
    newstring = newstring.replace("\"","")
    newstring = newstring.replace("{","")
    newstring = newstring.replace("}","")
    newstring = newstring.replace("[","")
    newstring = newstring.replace("]","")
    newstring = newstring.replace("<","")
    newstring = newstring.replace(">","")
    newstring = newstring.replace("~","")
    newstring = newstring.replace("`","")
    newstring = newstring.replace(":","")
    newstring = newstring.replace(";","")
    newstring = newstring.replace("|","")
    newstring = newstring.replace("\\","")
    newstring = newstring.replace("/","")        
    return newstring

def ArticleLength(articleName):
    tree = ec.parse(articleName) 
    root = tree.getroot()
    pageElement = root[1]

    for child in pageElement:
        if 'revision' in child.tag:
            for each in child:
                if 'text' in each.tag:
                    sentence = cleanString(each.text)
                    tagged_sent = pos_tag(sentence.split())
                    propernouns = [word for word,pos in tagged_sent if pos == 'NNP']
                    words_set = set(propernouns)
                    XML_article_len.append(len(words_set)) 



def ArticleLengthKML(articleName):
    tree = ec.parse(articleName) 
    root = tree.getroot()
    pageElement = root[0]

    for child in pageElement:
        if 'Instance' in child.tag:
            for each in child:
                if 'Body' in each.tag:
                    sentence = cleanString(each[0].text)
                    tagged_sent = pos_tag(sentence.split())
                    propernouns = [word for word,pos in tagged_sent if pos == 'NNP']
                    words_set = set(propernouns)
                    KML_article_len.append(len(words_set)) 


def main():
    ArticleLength(path)
    ArticleLengthKML(path2)
    # line 1 points 
    y1 = XML_article_len 
    x1 = [i+1 for i in range(len(XML_article_len))] 
    # plotting the line 1 points  
    plt.plot(x1, y1, label = "XML") 
      
    # line 2 points 
    y2 = KML_article_len 
    x2 = [i+1 for i in range(len(KML_article_len))] 
    # plotting the line 2 points  
    plt.plot(x2, y2, label = "KML", linestyle='dashed') 
      
    # naming the x axis 
    plt.xlabel('Revision number') 
    # naming the y axis 
    plt.ylabel('Number of Proper Nouns') 
    # giving a title to my graph 
    plt.title('Number of Proper Nouns vs Revision') 
      
    # show a legend on the plot 
    plt.legend() 
      
    plt.savefig('Number of Proper Nouns vs Revision')  
    # function to show the plot 
    plt.show() 

main()