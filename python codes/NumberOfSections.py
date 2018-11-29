import re
import xml.etree.cElementTree as ec
import os
import mwparserfromhell
import matplotlib.pyplot as plt
import numpy as np


path1 = "/home/paras/KML/resources/"
path2 = "/home/paras/KML/compressed-KML/"
FAfilenames = os.listdir(path1)
GAfilenames = os.listdir(path2)

featuredArticleList = []
goodArticleList = []

for filename in FAfilenames:
    if '.kml' in filename:
        featuredArticleList.append(path1+filename)

for filename in GAfilenames:
    if '.kml' in filename:
        goodArticleList.append(path2+filename)

# featuredArticleList = ['Arabian_Sea.xml']

def NumberOfSections(articleName):
    try:
        tree = ec.parse(articleName) 
        root = tree.getroot()
        count = 0

        for i in root.iter('Text'):
            count += len(re.findall(r'==([^=]+)==', i.text))

        return count

    except:
        print('\n'+'Error! in parsing '+articleName+'\n')
        return -1


def main():
    NumberOfSectionsListFA = []
    NumberOfSectionsListGA = []

    for articleName in featuredArticleList:
        result = NumberOfSections(articleName)
        if result != -1:
            NumberOfSectionsListFA.append(result)
    
    for articleName in goodArticleList:
        result = NumberOfSections(articleName)
        if result != -1:
            NumberOfSectionsListGA.append(result)
    
    print("KML")
    print("===")
    npArray = np.array(NumberOfSectionsListFA)
    print('Mean number of Sections ' + str(np.mean(npArray)))
    print('Standard Deviation ' + str(np.std(npArray)) + '\n')

    print("Compressed KML")
    print("==============")
    npArray = np.array(NumberOfSectionsListGA)
    print('Mean number of Sections ' + str(np.mean(npArray)))
    print('Standard Deviation ' + str(np.std(npArray)) + '\n')

main()