# coding=utf-8
import requests

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}
data = {
    "from": "zh",
    "to": "en",
    "query": "好好学习",
    "transtype": "translang",
    "simple_means_flag": "3",
    # sign会根据输入的值，计算结果，通过js生成
    "sign": "757602.1010771",
    "token": "ba52435d5b43bd9b6ef3579d8df1d35e"
}

post_url = "http://fanyi.baidu.com/v2transapi"

r = requests.post(post_url,data=data,headers=headers)
print(r)
print(r.content.decode())