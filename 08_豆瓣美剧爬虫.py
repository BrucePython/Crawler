# coding=utf-8
import requests
import json


class DoubanSpider:
    def __init__(self):
        self.url_temp_list = [
            {
                "url_temp": "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?&start={}&count=18&loc_id=108288",
                "country": "american"
            },
            {
                "url_temp": "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_english_hot/items?start={}&count=18&loc_id=108288",
                "country": "british"
            },
            {
                "url_temp": "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_domestic_hot/items?start={}&count=18&loc_id=108288",
                "country": "chinese"
            }
        ]
        # self.headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1", "Referer": "https://m.douban.com/tv/{}"}    # american

    def parse_url(self, url, headers):
        # 发送请求，获取响应
        print(url)
        response = requests.get(url, headers=headers)
        return response.content.decode()

    def get_content_list(self, json_str):
        # 提取是数据
        dict_ret = json.loads(json_str)
        content_list = dict_ret["subject_collection_items"]
        total = dict_ret["total"]
        return content_list, total

    def save_content_list(self, content_list,country):
        # 保存
        with open("douban.txt", "a", encoding="utf-8") as f:
            for content in content_list:
                content["country"] = country
                f.write(json.dumps(content, ensure_ascii=False))
                f.write("\n")  # 写入换行符，进行换行
        print("保存成功")

    def run(self):
        # 实现主要逻辑
        for url_temp in self.url_temp_list:
            num = 0
            total = 100  # 假设有第一页，假totle
            while num < total:     # 最后一条数据num+18，所以totle+18
                # 1.start_url
                url = url_temp["url_temp"].format(num)
                headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
                    "Referer": "https://m.douban.com/tv/{}".format(url_temp["country"])}

                # 2.发送请求，获取响应
                json_str = self.parse_url(url, headers)
                # 3.提取是数据
                content_list, total = self.get_content_list(json_str)   # 真totle

                # 4.保存
                self.save_content_list(content_list,url_temp["country"])
                # if len(content_list)<18:
                #   最后一页的数据条目小于18条
                #     break
                # 5.构造下一页的url地址,进入循环
                num += 18


if __name__ == '__main__':
    douban_spider = DoubanSpider()
    douban_spider.run()
