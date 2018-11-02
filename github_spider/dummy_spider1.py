import scrapy

f = open('haha.txt', "w")

class DummySpider(scrapy.Spider):
    name = "dummy"
    start_urls = [
        'https://github.com/jquery/jquery/commits/master',
    ]
    download_delay = 0.05



    def doit(self, response):
        arr = response.xpath('//tr//span/text()').extract()
        string = ""
        for stri in arr:
            string += stri
        yield {
            'insider': string,
        }

    def parse(self, response):
        for listitem in response.xpath('//li[@class="commit commits-list-item js-commits-list-item table-list-item js-navigation-item js-details-container Details js-socket-channel js-updatable-content"]'):
            rel_url = listitem.xpath('div/div/a/@href').extract_first()
            complete_url = response.urljoin(rel_url)
            yield {
                'about': listitem.xpath('div/p/a/text()').extract_first(),
                'author': listitem.xpath('div/div/div/a/text()').extract_first(),
                'datetime': listitem.xpath('div/div/div/relative-time/@datetime').extract_first(),
                'url': complete_url,
            }
            f.write(complete_url + '\n')
            #response.follow(rel_url, self.doit)

        next_page = response.xpath('//div/div/div/div/div/div/div/a/@href')[-1].extract()
        if next_page is not None:
            yield response.follow(next_page, self.parse)