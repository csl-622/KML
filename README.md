KML (Knowledge Markup Language)
===============================

What is KML?
------------
KML stands for Knowledge Markup Language, a standard format for storing the data of all the Knowledge Building Portals. Knowledge Building portals like Wikipedia, Stack Exchange, GitHub, e.t.c provides their data dump in their own formats. We are trying to propose a new standard format for all these types of portals such that the analysis is easy.

Need for KML
------------
All these Knowledge Building portals provide their data dumps in their own format. For example, Wikipedia provides its data in an XML format with their own schema definition. Similarly, Stack Exchange provides its data dump in an XML format with different schema definition. The KML will be a new standard format for these kinds of Knowledge Building portals with a standard schema definition. The idea is to make KML flexible enough such that it can store the data of any kind of Knowledge Building portals.

Components of this project
--------------------------

### KML-Compressor-Decompressor
Compresses text section of KML and decompresses any asked revision of article.

### KML-for-Github
Geneartes KML for github from scraped data in json format.

### Github-Spider
Scrapes data from Github and stores as json files.

### User-Agent-Spider
Scrapes many IP adressess to avoid blocking of scraper by Github.

### Wiki-Satck-KML-Downloader
Dowloads data from Wikipedia and Stackoverflow and then coverts it to KML.
