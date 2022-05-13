# https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx
#
# __VIEWSTATE: g9d+OUVrikkghT7JLxoyBS74z+8/xoRwVinh7czIKnff7p4JkiSu27eekWgQh1gEhkLBEk0IXpihsi14oZBEoJup3JqzMM38xt5nrW5A32oyrNXZ46jWDw+Ur9I=
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://so.gushiwen.cn/user/collect.aspx
# email: 45745554@qq.com
# pwd: 123435446
# code: 071j
# denglu: 登录

import requests
url='https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'

headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'

}
response=requests.get(url=url,headers=headers)
content=response.text
# print(content)

# 解析： __VIEWSTATE:    __VIEWSTATEGENERATOR:
from bs4 import BeautifulSoup
soup=BeautifulSoup(content,'lxml')


# 获取   __VIEWSTATE:    __VIEWSTATEGENERATOR:
viewstate=soup.select('#__VIEWSTATE')[0].attrs.get('value')
viewstategenerator=soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')
# print(viewstate)
# print(viewstategenerator)


# 获取验证码图片
code=soup.select('#imgCode')[0].attrs.get('src')
# print(code)
code_url='https://so.gushiwen.cn/'+code
# print(code_url)

#有坑（获取验证码是一次，登录时验证码又执行一次，再次刷新）
# import urllib.request
# 下载验证码
# urllib.request.urlretrieve(url=code_url,filename='24.jpg')
# requests里有一个方法session（），通过session（） 的返回值就能使用请求变成一个对象
session=requests.session()
# 验证码的url的内容
response_code=session.get(code_url)
# 注意：此时使用二进制数据
content_code=response_code.content
# wb模式就是将二进制写入文件
with open('24.jpg','wb') as f:
    f.write(content_code)

#获取验证码的图片之后  下载到本地 然后观察验证码  然后在控制台输入验证码
code_name=input("请输入你的验证码：")
url_post='https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
data_post={
    '__VIEWSTATE':viewstate,
    '__VIEWSTATEGENERATOR':viewstategenerator,
    'from':'http://so.gushiwen.cn/user/collect.aspx',
    'email':'账号',  #这里是账号
    'pwd':'密码',        #这里是密码
    'code':code_name,
    'denglu':'登录'
}
response_post=session.post(url=url,headers=headers,data=data_post)
content_post=response_post.text
with open('24.html','w',encoding='utf-8') as f:
    f.write(content_post)


# 难点：
# 1.隐藏域
# 2.验证码