# coding=utf-8
import requests
import re

url = "https://www.guokr.com/ask/highlight/"
# headers = {"Referer": "https://m.guokr.com/ask/","User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
headers = {"Referer": "https://www.guokr.com/ask/","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}
response = requests.get(url,headers=headers)
html_str = response.content.decode()
# print(html_str)
#提取第一页的数据
# content = re.findall(r'<h3 class="list-title">(.*?)</h3>',html_str,re.S)      # 手机版
# content = re.findall(r'<a target="_blank" href="(.*?)">(.*?)</a>',html_str,re.S)
content = re.findall(r"<h2><a target=\"_blank\" href=\"(.*?)\">(.*?)</a></h2>",html_str,re.S)
# https://www.guokr.com/question/669761/
print(content)