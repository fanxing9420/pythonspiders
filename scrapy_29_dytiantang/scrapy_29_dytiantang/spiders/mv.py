import scrapy
from scrapy_29_dytiantang.items import Scrapy29DytiantangItem

class MvSpider(scrapy.Spider):
    name = 'mv'
    allowed_domains = ['www.ygdy8.net']
    start_urls = ['https://www.ygdy8.net/html/gndy/china/index.html']

    def parse(self, response):
        # pass
        a_list=response.xpath('//div[@class="co_content8"]//td[2]//a[2]')

        for a in a_list:
            #获取第一页的name和要点的链接
            name=a.xpath('./text()').extract_first()
            href=a.xpath('./@href').extract_first()


            #第二页地址是
            url='https://www.ygdy8.net/'+href
            # print(url)
            yield scrapy.Request(url=url,callback=self.parse_second,meta={'name':name})

    def parse_second(self,response):
        #注意：拿不到数据,查看xpath语法是否正确，有些标签是不能够被识别的
        src=response.xpath('//div[@id="Zoom"]//img/@src').extract_first()
        name=response.meta['name']
        movie=Scrapy29DytiantangItem(src=src,name=name)
        yield movie