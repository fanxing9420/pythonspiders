import scrapy
from scrapy_28_dangdang.items import Scrapy28DangdangItem

class DangSpider(scrapy.Spider):
    name = 'dang'
    allowed_domains = ['category.dangdang.com']
    start_urls = ['http://category.dangdang.com/cp01.03.44.00.00.00.html']
    #http://category.dangdang.com/pg2-cp01.03.44.00.00.00.html
    # http://category.dangdang.com/pg3-cp01.03.44.00.00.00.html
    base_url="http://category.dangdang.com/pg"
    page=1
    def parse(self, response):
        # pipelines 下载数据
        # items 定义数据结构


        li_list=response.xpath('//ul[@id="component_59"]/li')
        for li in li_list:
            src=li.xpath('.//img/@data-original').extract_first()
            if src:
                src=src
            else:
                src=li.xpath('.//img/@src').extract_first()
            name=li.xpath('.//img/@alt').extract_first()
            price=li.xpath('.//p[@class="price"]/span[1]/text()').extract_first()
            print(src,name,price)
            # pass
            book=Scrapy28DangdangItem(src=src,name=name,price=price)
            yield book

        if self.page<100:
            self.page=self.page+1
            url=self.base_url+str(self.page)+'-cp01.03.44.00.00.00.html'
            yield   scrapy.Request(url=url,callback=self.parse)