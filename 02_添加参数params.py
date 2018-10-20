import requests


# 发送一个带header的请求


# 发送一个带参数的请求
# params = {"wd": "天天向上"}

# # 带不带问号都一样
# # url_temp = "https://www.baidu.com/s?"
# url_temp = "https://www.baidu.com/s"

# r = requests.get(url_temp, headers=headers, params=params)


# 用format格式化简写带参数的请求
url = "https://www.baidu.com/s?wd={}".format("天天向上")
r = requests.get(url, headers=headers)
print(r.status_code)
print(r.request.url)



