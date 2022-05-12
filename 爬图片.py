import urllib.request
from lxml import etree

# https://sc.chinaz.com/tupian/qinglvtupian.html
# https://sc.chinaz.com/tupian/qinglvtupian_2.html

# https://www.igdcc.com/4Kyouxi/index_238.html
# https://www.igdcc.com/shouji/

# https://www.bizhi88.com/3840x2160/
# https://www.bizhi88.com/3840x2160/2.html

# https://www.tooopen.com/tag/5b6bd00febc8b20da8df60a9.aspx?
# https://www.tooopen.com/tag/5b6bd00febc8b20da8df60a9.aspx?page=2
# 看上面举例的链接，页码，然后在url中改动相关代码
def create_request(page):
    if(page==1):
        url='https://www.meituzm.com/category/mm/'
    else:
        url='https://www.meituzm.com/category/mm/?page='+str(page)
        print(url)

    headers={
        'user-agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29',
        'cookie':'PHPSESSID = bgodev3mmgnkp9f73gu55122v4;Hm_lvt_fe338b12aba190ae800147b6d1d0d309 = 1649423981;Hm_lpvt_fe338b12aba190ae800147b6d1d0d309 = 1649431013',

    }
    request=urllib.request.Request(url=url,headers=headers)
    return request

def get_content(request):
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    return content

def down_load(content):
    # urllib.request.urlretrieve('图片地址','文件名字')
    tree=etree.HTML(content)
    name_list=tree.xpath('//div[@id="content"]//ul//a/img/@alt')
    src_list=tree.xpath('//div[@id="content"]//ul//a/img/@src')
    for i in range(len(name_list)):
        name=name_list[i]
        src=src_list[i]
        url=src
        urllib.request.urlretrieve(url=url,filename='./素材公社性感写真/'+name+'.jpg')
        print(url)
if __name__=='__main__':
    start_page=int(input("开始："))
    end_page = int(input("结束："))

    for page in range(start_page,end_page+1):
        # print(page)
        request=create_request(page)
        content=get_content(request=request)
        down_load(content)