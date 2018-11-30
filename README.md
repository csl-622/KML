KML (Knowledge Markup Language)
===============================

What is KML?
------------
KML stands for Knowledge Markup Language, a standard format for storing the data of all the Knowledge Building Portals. Knowledge Building portals like Wikipedia, Stack Exchange, GitHub, e.t.c provides their data dump in their own formats. We are trying to propose a new standard format for all these types of portals such that the analysis is easy.

![alt text](https://github.com/csl-622/KML/blob/master/images/every.png)


Need for KML
------------
All these Knowledge Building portals provide their data dumps in their own format. For example, Wikipedia provides its data in an XML format with their own schema definition. Similarly, Stack Exchange provides its data dump in an XML format with different schema definition. The KML will be a new standard format for these kinds of Knowledge Building portals with a standard schema definition. The idea is to make KML flexible enough such that it can store the data of any kind of Knowledge Building portals.

Components of this project
--------------------------

### KML-Compressor-Decompressor
These programs compresses and decompresses a KML file using diff algorithm inspired from git. It can compress the KML file by 30% or more depending upon the edits made on an article. The compressed KML is also very easy to read, since the number of lines is reduced from 1 lakh to 9k and it retains the original structure of the KML so that it remains readable even when compressed.

### KML-for-Github
We had to make KML for github and we had KML for wikipedia earlier. The attempt of this program is to retain the structure of KML for wkipedia while representing all the data in a git workflow in this newly generated KML file. We achived this by viewing each commit as a revision of an article on wikipedia. The revisions are not compressed unlike KML for wikipedia because the commits can be highly unrelated.

### Github-Spider
This multithreaded web-spider follows the rules of /robots.txt file and is useful for fetching small sized GitHub repositories. It outputs the results in JSON format.

### Github-Spider-Proxy-Rotated
Github-Spider-Proxy-Rotated is an advanced version of the previous spider; it contains pipelines, middlewares,
and throttling parameters, which is in the middleware and settings file. This spider is for advanced scraping.
It has a bottleneck mechanism for limiting the number of HTTP requests per second, and also a technique for
HTTP headers rotation. It outputs the results in JSON format.

### User-Agent-Spider
This spider gets the latest user-agent headers from an online forum, output of this file is directly put into use in other two spiders namely Github-Spider and Github-Spider-Proxy-Rotated. The result of this spider is a text file containing a list of HTTP headers which can is useful for spoofing browser's  HTTP request activity.

### Wiki-Satck-KML-Downloader
Dowloads xml from Wikipedia and Stackexchange for any given topic from user then coverts it to KML. The topics for wikipedia can be name of any page on wikipedia like UNO while for stackexchange the topics can any of the sub-site name of stackexchange like beer for beer.stackexchange.com, all these sites are listed in site_list.txt inside Wiki-Stack-KML-Downloader folder.

### Analysis
Graphs are generated to compare compressed KML and XML on various performance metrics like change in ArticleLength Vs Revision for KML and XML files which are plotted on same graph. Similarly, we have performed analysis based on change in Number of revisons, Number of Images, Number of Nouns (using natural language processing module nltk), Number of sections etc VS Revision number and all these graphs are stored in AnalysisFig folder. 
Finally, we plotted the running time of these analysis functions for compressed XML and KML documnets and plotted on the same graph to show how a compressed KML can improve the runtime of various analysis functions with respect to a simple XML.
