    # -*- coding: utf-8 -*-
import tkinter
import xml.etree.cElementTree as ec
import matplotlib.pyplot as plt
import os
from FeaturedDate import GetFeaturedArticleDate 

path = os.getcwd()
path1 = "/home/paras/KML/resources"
filenames = os.listdir(path1)

path2 = "/home/paras/KML/compressed-KML"
filenames2 = os.listdir(path2)

featuredArticleList1 = []
featuredArticleList2 = []
for filename in filenames:
    if '.kml' in filename:
        featuredArticleList1.append(filename)

for filename in filenames2:
    if '.kml' in filename:
        featuredArticleList2.append(filename)

#featuredArticleList = ['/home  /descentis/research/WikiMeter/analysis/wiki_analysis/wiki_data/Zinc.xml']
    
def PlotChangeInSizeGraph(articleName, FeaturedDate,num):
    tree = ec.parse(articleName) 
    root = tree.getroot()
    
    
    SizeOfArticle = 0
    ChangeInArticle = 0
    MaxChange = 0
    MaxChangeDate = ''
    previousSize = 0
    PastChangeInSize = 0
    dateTemp = []
    Pastdate = 0
    count = 0
    error = 0
    yAxis = []
    xAxis = []
    
    for i in root.iter('CreationDate'):
        print(i.text)
        dateTemp.append(int(i.text[0:10].replace('-', '')))

    count = 0
    for each in root.iter('Text'):
        if(len(each.text) != 0):
            SizeOfArticle = len(each.text)
            ChangeInArticle = SizeOfArticle - previousSize
            tempCalc = int(0.1*abs(PastChangeInSize))
            if abs(ChangeInArticle) in range(abs(PastChangeInSize)-tempCalc, abs(PastChangeInSize)+tempCalc+1) and abs(ChangeInArticle) >= 100 and (ChangeInArticle*PastChangeInSize) < 0:
                yAxis.pop()
                xAxis.pop()
                count -= 1
                error = ChangeInArticle
                print('Revert Found!')

            else:
                yAxis.append(ChangeInArticle)
                count += 1
                xAxis.append(count)
                if PastChangeInSize > MaxChange and error != PastChangeInSize:
                    MaxChange = PastChangeInSize
                    MaxChangeDate = Pastdate
                        #print(ChangeInArticle, count, SizeOfArticle, PastChangeInSize,'\n','\n')

                #print(ChangeInArticle, count, SizeOfArticle, PastChangeInSize)
            previousSize = SizeOfArticle
            PastChangeInSize = ChangeInArticle
            Pastdate = dateTemp[count]
            count += 1

    					
    
    	#print(MaxChangeDate, MaxChange, articleName, FeaturedDate)
    plt.plot(xAxis, yAxis, 'r-')
    plt.xlabel('Number of Intervals')
    plt.ylabel('Change in Bytes')
    plt.title('Change in size over time of ' + articleName)
    plt.savefig('change_in_bytes_plot/plot'+str(num)+'.png',dpi=800)


    plt.show()
    
def main():
    num = 1
    for i,j in zip(featuredArticleList1,featuredArticleList2): #For each featured article get the starting time
        FeaturedDate = GetFeaturedArticleDate(i)
        PlotChangeInSizeGraph(j, FeaturedDate,num)
        num+=1			
    
main()
