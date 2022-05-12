# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import urllib.request

from itemadapter import ItemAdapter


class Scrapy28DangdangPipeline:
    def open_spider(self,spider):
        # 在爬虫文件开始之前就执行的一个方法
        self.fp=open('book.json','w',encoding='utf-8')
        # item就是yield后面的book对象
    def process_item(self, item, spider):
        # 以下这种模式，每传递过来一个对象，就会打开一次文件，对文件操作过于频繁
        # (1)write 必须是字符串
        # (2) a 模式是追加  w模式是覆盖
        # with open('book.josn','a',encoding='utf-8') as fp:
        #     fp.write(str(item))
        self.fp.write(str(item))
        return item
        # 在爬虫文件执行完之后  执行的方法
    def close_spider(self,spider):
        self.fp.close()


#多条管道同时开启
# (1)定义管道类
#（2）在setting中开启管道
#  'scrapy_28_dangdang.pipelines.DangDangDownloadPipeline': 301,
class DangDangDownloadPipeline:
    def process_item(self,item,spider):
            url='http:'+item.get("src")
            filename='./books/'+item.get("name")+'.jpg'
            urllib.request.urlretrieve(url=url,filename=filename)
            return item