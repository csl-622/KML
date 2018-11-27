import requests
import os
import numpy as np
from bs4 import BeautifulSoup

path = os.getcwd()
# path = path + '/WikiData/GoodArticles/'
filenames = os.listdir(path)

featuredArticleList = []
for filename in filenames:
    if '.xml' in filename:
        # filename = path + filename
        featuredArticleList.append(filename)

# featuredArticleList = ['Arabian Sea.xml']

def NumberOfReferences(articleName):
	url = 'https://en.wikipedia.org/wiki/' + articleName
	headers = {
		'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Mobile Safari/537.36'
	}

	r = requests.get(url, headers=headers)

	# try:
	if r.status_code == 200:
		html = r.text
		soup = BeautifulSoup(html, 'lxml')

		count = 0
		for link in soup.find_all('ol','references'):
			for child in link:
				if child.name != None:	
					count += 1

		print(articleName + ' ' + str(count))
		return count

	else:
		print('\n' + 'Error! ' + articleName + '\n')
		return -1

	# except:
	# 	print('\n' + 'Error! ' + articleName + '\n')
	# 	return -1

def main4():
	numberOfReferencesList = []
	references = 0
	for articleName in featuredArticleList:
		articleName = articleName[:-4]
		# articleName = articleName.split('/')[-1]
		references = NumberOfReferences(articleName)
		if references != -1:
			numberOfReferencesList.append(references)

	numberOfReferencesList = np.array(numberOfReferencesList)
	print(str(np.mean(numberOfReferencesList)) + ' ' + str(np.std(numberOfReferencesList)))

main4()