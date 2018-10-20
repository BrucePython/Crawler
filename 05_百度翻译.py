# 电脑版的有些字段不能整，看手机版的
# coding=utf-8
import requests
import json
# 实现用户即时翻译：
import sys

"""
# 在终端输入python 05_百度翻译.py 1 2
print(sys.argv)
# 输出：['05_百度翻译.py', '1', '2']
# 所以，可以用来取值：sys.argv[0] = '05_百度翻译.py', sys.argv[1] = 1
"""

# 实现自定义的翻译内容: 中文 to 英文
query_string = sys.argv[1]

# 用alias命令，给某些命令取别名
# 实现终端输入：fanyi 你好，而不用：python 05_百度翻译.py 你好
# emacs ~/.bashrc, 在bash rc里面修改alias  fanyi= 等号前后无空格
# source ~/.bashrc


# 让程序自动根据输入的内容，判断zh to en或en to zh，浏览器通过langdetect判断
# 调用langdetect接口，判断输入的内容是中/英文

headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
post_data = {
    "query": query_string,
    "from": "zh",
    "to": "en"
}

# 找url地址：从前往后找，不是js和css图片的内容
post_url = "http://fanyi.baidu.com/basetrans"

r = requests.post(post_url, data=post_data, headers=headers)
# print(r.content.decode())

# 转换成字典，提取里面的内容: import json
dict_ret = json.loads(r.content.decode())
# 提取字典里的内容：提取dst的值
ret = dict_ret["trans"][0]["dst"]
print("result is: ", ret)
