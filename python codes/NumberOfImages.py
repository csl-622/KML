# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ec
import numpy as np
import matplotlib.pyplot as plt
import os

path1 = "/home/paras/KML/resources/"
path2 = "/home/paras/KML/compressed-KML/"
FAfilenames = os.listdir(path1)
GAfilenames = os.listdir(path2)

featuredArticleList = []
goodArticleList = []
for filename in FAfilenames:
    if '.kml' in filename:
        filename = path1 + filename
        featuredArticleList.append(filename)
        
for filename in GAfilenames:
    if '.kml' in filename:
        filename = path2 + filename
        goodArticleList.append(filename)

# featuredArticleList = ['Arabian_Sea.xml']

def CurrentText(articleName):
	try:
		tree = ec.parse(articleName) 
		root = tree.getroot()

		latestRevisionText = ''

		for each in root.iter('Text'):
				latestRevisionText = each.text

		return latestRevisionText
	except:
		print('\n'+'Error! in parsing '+articleName+'\n')
		return -1

def NumberOfImages(currentText, articleName):
	imageFormates = ['.jpg','.jpeg','.svg','.gif','.png','.bmp','.tiff']
	try:
		count = 0
		for image in imageFormates:
			count += currentText.count(image)	
		print(articleName + ' ' + str(count))	
		return count

	except:
		print('\n'+'Something went wrong!'+articleName+'\n')
		return -1

def main():
    listOfImagesFA = []
    listOfImagesGA = []

    for articleName in featuredArticleList: 
        currentText =  CurrentText(articleName)
        if currentText != -1:
            listOfImagesFA.append(NumberOfImages(currentText, articleName))

    for articleName in goodArticleList: 
        currentText =  CurrentText(articleName)
        if currentText != -1:
            listOfImagesGA.append(NumberOfImages(currentText, articleName))

    print("KML")
    print("===")
    npArray = np.array(listOfImagesFA)
    print('Mean number of Images ' + str(np.mean(npArray)))
    print('Standard Deviation ' + str(np.std(npArray)) + '\n')

    print("Compressed KML")
    print("==============")
    npArray = np.array(listOfImagesGA)
    print('Mean number of Images ' + str(np.mean(npArray)))
    print('Standard Deviation ' + str(np.std(npArray)) + '\n')

main()