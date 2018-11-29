# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ec
import numpy as np
import os

path = "/home/paras/KML/resources"
path2 = "/home/paras/KML/compressed-KML"
# path = path + '/WikiData/GoodArticles/'
filenames = os.listdir(path)
filenames2 = os.listdir(path2)

featuredArticleListKML = []
featuredArticleListKML2 = []

for filename in filenames:
    if '.kml' in filename:
        filename = path+'/'+filename
        featuredArticleListKML.append(filename)

for filename in filenames2:
    if '.kml' in filename:
        filename = path2+'/'+filename
        featuredArticleListKML2.append(filename)

def ArticleLengthKML(articleName):
	tree = ec.parse(articleName) 
	root = tree.getroot()


	pageElement = root[0]
	total = 0
	contributors = {}
	sizeOfArticle = 0
	count = 0

	for i in root.iter('Text'):
		sizeOfArticle += len(i.text)
		count += 1

	return sizeOfArticle

def main():
	listOfResultsKML = []
	listOfResultsKML2 = []

	print("KML")
	print("===")

	for articleName in featuredArticleListKML: 
		result = ArticleLengthKML(articleName)
		if result != -1:
			listOfResultsKML.append(result) 

	print("Compressed KML")
	print("==============")

	for articleName in featuredArticleListKML2: 
		result = ArticleLengthKML(articleName)
		if result != -1:
			listOfResultsKML2.append(result) 

	print("KML")
	print("===")
	npArray = np.array(listOfResultsKML)
	print('Mean length of articles ' + str(np.mean(npArray)))
	print('Standard Deviation ' + str(np.std(npArray)) + '\n')

	print("Compressed KML")
	print("==============")
	npArray = np.array(listOfResultsKML2)
	print('Mean length of articles ' + str(np.mean(npArray)))
	print('Standard Deviation ' + str(np.std(npArray)) + '\n')

main()