import scrapy


class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = ['xz.58.com']
    start_urls = ['http://xz.58.com/']

    def parse(self, response):
        content=response.body
        print("==============")
        print(content)
        pass
