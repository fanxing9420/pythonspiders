import urllib.request
import urllib.parse
def create_request(page):

    base_url = "https://movie.douban.com/top250?"
    data={
        'start':(page-1)*25,
        'filter':20
        }


    data= urllib.parse.urlencode(data)
    url = base_url + data
    print(url)
    headers={
        # 'User - Agent': 'Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 99.0.4844.51Safari / 537.36Edg / 99.0.1150.39'
        'Cookie': 'll="118161"; bid=5cBVpNqid80; _vwo_uuid_v2=D45E4E4B1EAE7035F4686A86B9A0C0134|17ac109a1ce3a940cd607eea69989c60; __utmc=30149280; __utmc=223695111; ap_v=0,6.0; __gads=ID=032c05146012f52c-22deaa68eed10084:T=1649916778:RT=1649916778: S=ALNI_MZ6cKzkpPoKMyiGFtLc6oVMSvkQww; __utma=30149280.638397394.1649408408.1649916715.1649920526.3; __utmb=30149280.0.10.1649920526; __utmz=30149280.1649920526.3.3.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.1472431755.1649408412.1649916715.1649920526.3; __utmb=223695111.0.10.1649920526; __utmz=223695111.1649920526.3.3.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1649920526%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_id.100001.4cf6=826d7eb61914769a.1649408412.3.1649920526.1649917562.; _pk_ses.100001.4cf6=*',
        'DNT': ' 1',
        'Host': ' movie.douban.com',
        'Referer':' https://cn.bing.com/',
        'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.36',
    }
    request=urllib.request.Request(url=url,headers=headers)
    return request
def get_content(request):
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    return content
def download(page,content):
    with open('./豆瓣top250/douban_'+str(page)+'.json','w',encoding='utf-8')as fp:
        fp.write(content)

if __name__ == '__main__':
    start_page = int(input('请输入开始：'))
    end_page = int(input('请输入结束：'))
    for page in range(start_page,end_page+1):
         request=create_request(page)
         content=get_content(request)
         download(page,content)
