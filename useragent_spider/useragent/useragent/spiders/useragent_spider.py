import scrapy

f = open("user_final.txt", "w")


class QuotesSpider(scrapy.Spider):
    name = "nitin_useragent"

    def start_requests(self):
        urls = [
            'http://www.useragentstring.com/pages/useragentstring.php?name=Opera',
            'http://www.useragentstring.com/pages/useragentstring.php?name=Chrome',
            'http://www.useragentstring.com/pages/useragentstring.php?name=Firefox',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        elem = response.xpath('//ul/li/a[text()]/text()').extract()
        for item in elem:
            f.write(str(item) +"\n")