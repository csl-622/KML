import scrapy

f = open('haha.txt', "r")

#urls = [line for line in f]
'''
for k in urls:
    print(k)file js-file js-details-container
'''


class DummySpider(scrapy.Spider):
    flag = 0
    global urls
    name = "dummy"
    start_urls = [line.strip() for line in f]


    def parse(self, response):
        if(response.status == 409):
            self.flag = 1
        if(self.flag == 0):
            abc = response.xpath('//*[contains(@class, "file js-file js-details-container")]')
            dictionary = {}
            count = 0
            for item in abc:
                one = item.xpath('div//*[contains(@class, "link-gray-dark")]/@title').extract_first()
                two = item.xpath('div/div/table/tr/td/span/span/text()').extract()
                twocode = ""
                for word in two:
                    twocode += word + " "
                dictionary[one] = twocode
                count = count + 1
            dictionary['count'] = count
            yield{
                'dictionary': dictionary,
            }
