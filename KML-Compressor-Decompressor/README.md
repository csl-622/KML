KML Compressor Decompressor
===========================
These programs compresses and decompresses a KML file using diff algorithm inspired from git. It can compress the KML file by 30% or more depending upon the edits made on an article. The compressed KML is also very easy to read, since the number of lines is reduced from 1 lakh to 9k and it retains the original structure of the KML so that it remains redable even when compressed.

compressor.py
=============
It compresses the text portion of KML file while retaining it's original structure. It also improves the readablity of the KML file 
because it greatly reduces the number of lines.

Usage: run this script using python3 then you will be asked to enter the KML file name.

decompressor.py
===============
It generates the nth decompressed revision from the compressed kml file. 

Usage: run this script using python3 then you will be asked to enter the KML file name and value of n.
