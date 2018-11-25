#!/bin/bash

echo "executing::python first.py"  
python first.py

echo "executing::scrapy runspider dummy_spider1.py -o dummy1.json --nolog"  
scrapy runspider dummy_spider1.py -o dummy1.json --nolog

echo "executing::scrapy runspider dummy_spider2.py -o dummy2.json --nolog"  
scrapy runspider dummy_spider2.py -o dummy2.json --nolog


echo "Output files: dummy1.json | dummy2.json | haha.txt"