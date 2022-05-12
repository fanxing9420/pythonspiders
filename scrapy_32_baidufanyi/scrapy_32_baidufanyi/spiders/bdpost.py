import scrapy
import json

class BdpostSpider(scrapy.Spider):
    name = 'bdpost'
    allowed_domains = ['fanyi.baidu.com']
    # post请求 没有参数 那么这个请求没有意义
    # 所以start_url也没有用了
    # parse也没有用了
    # start_urls = ['https://fanyi.baidu.com/sug']
    #
    # def parse(self, response):
    #     pass

    def start_requests(self):
        url='https://fanyi.baidu.com/sug'

        data={
            'kw':'final'
        }
        yield scrapy.FormRequest(url=url,formdata=data,callback=self.parse_second)

    def parse_second(self, response):
        content=response.text
        obj=json.loads(content)
        print(obj)