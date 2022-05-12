import requests, json


class Tencent(object):
    def __init__(self):
        self.base_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?'
        self.headers = {
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'referer': 'https://careers.tencent.com/search.html'
        }

        self.parse()

    def parse(self):
        for i in range(1, 3):
            params = {
                'timestamp': '1572850838681',
                'countryId': '',
                'cityId': '',
                'bgIds': '',
                'productId': '',
                'categoryId': '',
                'parentCategoryId': '',
                'attrId': '',
                'keyword': '',
                'pageIndex': str(i),
                'pageSize': '10',
                'language': 'zh-cn',
                'area': 'cn'
            }
            response = requests.get(self.base_url, headers=self.headers, params=params)#作为参数的传递
            self.parse_json(response.text)

    def parse_json(self, text):
        # 将json字符串编程python内置对象
        infos = []
        json_dict = json.loads(text)
        for data in json_dict['Data']['Posts']:
            RecruitPostName = data['RecruitPostName']
            CategoryName = data['CategoryName']
            Responsibility = data['Responsibility']
            LastUpdateTime = data['LastUpdateTime']
            detail_url = data['PostURL']
            item = {}
            item['RecruitPostName'] = RecruitPostName
            item['CategoryName'] = CategoryName
            item['Responsibility'] = Responsibility
            item['LastUpdateTime'] = LastUpdateTime
            item['detail_url'] = detail_url
            # print(item)
            infos.append(item)
        self.write_to_file(infos)

    def write_to_file(self, list_):
        for item in list_:
            with open('infos.txt', 'a+', encoding='utf-8') as fp:
                fp.writelines(str(item))


if __name__ == '__main__':
    t = Tencent()

