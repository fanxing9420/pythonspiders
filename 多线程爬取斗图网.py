import requests
import queue
import os
from lxml import etree
import urllib.request
import threading
class Producer(threading.Thread):
    headers={
        'user - agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 86.0.4240.198Safari / 537.36'
    }

    def __init__(self,q1,q2,*args,**kwargs):
        super(Producer,self).__init__(*args,**kwargs)
        self.q1=q1
        self.q2=q2

    def run(self):
        while True:
            if self.q1.empty():
                break
            url=self.q1.get()
            self.parse_page(url)

    def parse_page(self,url):
        response=requests.get(url=url,headers=self.headers).text
        tree=etree.HTML(response)
        div_list=tree.xpath('//div[@class="page-content"]/a')[1:]
        for div in div_list:
            img_url='https://dou.yuanmazg.com/'+div.xpath('./img/@data-original')[0]
            houzhui=img_url.split(".")[-1]
            img_name=div.xpath('./img/@alt')[0]
            end_name=img_name+'.'+houzhui
            self.q2.put((img_url,end_name))
        # pass

class Consumer(threading.Thread):
    os.makedirs("表情包下载",exist_ok=True)
    def __init__(self,q1,q2,*args,**kwargs):
        super(Consumer,self).__init__(*args,**kwargs)
        self.q1=q1
        self.q2=q2

    def run(self):
        while True:
            if self.q1.empty() and self.q2.empty():
                break
            img_url,end_name = self.q2.get()
            urllib.request.urlretrieve(url=img_url,filename='./表情包下载/%s' % end_name)
def main():
    q1=queue.Queue(1000)
    q2=queue.Queue(1000)
    urls=[]
    start_page=int(input('开始：'))
    end_page=int(input('结束：'))
    for page in range(start_page,end_page+1):
        url=f'https://dou.yuanmazg.com/doutu?page={page}'
        urls.append(url)

    for i in urls:
        q1.put(i)

    t1=Producer(q1,q2)
    t1.start()
    t2=Consumer(q1,q2)
    t2.start()

if __name__=='__main__':
    main()

