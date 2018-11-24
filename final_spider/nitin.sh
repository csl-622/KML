#!/usr/bin/env bash


echo "::Entering the first directory::"
cd git_final_spider
echo "::Clearing dummy1.json::"
rm dummy1.json
echo "::Clearing urls::"
rm haha.txt
echo "::Starting crawling::"
scrapy crawl git_1 -o dummy1.json --nolog
echo "::getting url files::"
cd ../git_final_spider_2/git_final_spider/
rm haha.txt
echo "::url pipeline::"
cd ../../git_final_spider
echo "::urls import finished::"
cp haha.txt ../git_final_spider_2/git_final_spider/
cd ../git_final_spider_2/git_final_spider/
echo "::running final spider::"
scrapy crawl git_2 -o dummy2.json --nolog