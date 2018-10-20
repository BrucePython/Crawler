# coding=utf-8
import requests
import json
import sys

class BaiduFanyi(object):
    def __init__(self, trans_str):
        self.lang_detect_url = "http://fanyi.baidu.com/langdetect"
        self.trans_url = "http://fanyi.baidu.com/basetrans"
        self.trans_str = trans_str
        self.headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}

    def parse_url(self,url,data):
        # 1.2) 发送post请求，获取响应
        response = requests.post(url, headers=self.headers, data=data)
        # return response.content.decode()    # 得到的是字符串，要把这个字符串转化成字典
        return json.loads(response.content.decode())

    def get_ret(self, dict_response):
        # 提取翻译结果
        ret = dict_response["trans"][0]["dst"]
        # print("result is: ",ret)
        print("{} 翻译后的结果: {}". format(self.trans_str, ret))

    def run(self):
        # 1. 获取语言类型
        #   1.1) 准备【语言检测】的post的url地址，post_data
        lang_detect_data = {"query": self.trans_str}
        #   1.2) 发送post请求，获取响应; 1.3) 提取语言类型. {"error":0,"msg":"success","lan":"zh"}
        lang = self.parse_url(self.lang_detect_url, lang_detect_data)["lan"]
        # 2. 准备【翻译】的post数据
        trans_data = {"query": self.trans_str,"from": "zh", "to": "en"} if lang == "zh" else {"query": self.trans_str,"from": "en", "to": "zh"}
        # 3. 发送请求，获取响应
        dict_response = self.parse_url(self.trans_url, trans_data)
        # 4. 提取翻译的结果
        return self.get_ret(dict_response )

if __name__ == '__main__':
    trans_str = sys.argv[1]
    "https://www.baidu.com/s?wd=%E6%9D%8E%E6%AF%85"
    baidu_fanyi = BaiduFanyi(trans_str)
    baidu_fanyi.run()
