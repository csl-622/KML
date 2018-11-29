import requests
import os
import numpy as np
import xml.etree.cElementTree as ec

path1 = "/home/paras/KML/resources/"
path2 = "/home/paras/KML/compressed-KML/"
FAfilenames = os.listdir(path1)
GAfilenames = os.listdir(path2)

featuredArticleList = []
featuredArticleList2 = []
for filename in FAfilenames:
    if '.kml' in filename:
        filename = path1 + filename
        featuredArticleList.append(filename)
        
for filename in GAfilenames:
    if '.kml' in filename:
        filename = path2 + filename
        featuredArticleList2.append(filename)


def NumberOfReferences(articleName):
	tree = ec.parse(articleName) 
	root = tree.getroot()
	count = 0
	for each in root.iter('Text'):
			if each.find("==References==") != -1:
				count += 1
	return count


def main4():
	numberOfReferencesList = []
	references = 0
	for articleName in featuredArticleList:
		references = NumberOfReferences(articleName)
		if references != -1:
			numberOfReferencesList.append(references)

	npArray = np.array(numberOfReferencesList)
	print("KML")
	print("===")
	print('Mean number of Refrences ' + str(np.mean(npArray)))
	print('Standard Deviation ' + str(np.std(npArray)) + '\n')

	numberOfReferencesList2 = []
	references2 = 0
	for articleName in featuredArticleList2:
		references2 = NumberOfReferences(articleName)
		if references2 != -1:
			numberOfReferencesList2.append(references)

	npArray = np.array(numberOfReferencesList2)
	print("Compressed KML")
	print("==============")
	print('Mean number of References ' + str(np.mean(npArray)))
	print('Standard Deviation ' + str(np.std(npArray)) + '\n')

main4()