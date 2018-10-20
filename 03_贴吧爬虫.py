# 1. 请求一千个url地址，需要一个url列表
# 只要是文本格式（只输出字符串）的文件，用w；否则都用wb
import requests

# 抽象成一个类，面向对象；干一件事情，抽成一个方法
# 抽象成一个函数，面向过程

class TiebaSpider():
    def __init__(self, tieba_name):
        self.url_temp = "https://tieba.baidu.com/f?kw="+ tieba_name+"&ie=utf-8&pn={}"
        self.headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36"}
        self.tieba_name = tieba_name

    def get_url_list(self):
        '''构造url列表'''
        # url_list = []
        # for i in range(1000):
        #     url_list.append(self.url_temp.format(i*50))
        # return url_list
        return [self.url_temp.format(i*50) for i in range(1000)]


    def parse_url(self,url):
        '''发送请求,获取响应'''
        response = requests.get(url,headers=self.headers)
        # 返回响应字符串
        return response.content.decode()

    def save_html(self,html_str,page_num):
        '''保存html字符串'''
        file_path = "{}-第{}页.html".format(self.tieba_name,page_num)
        with open(file_path,"w", encoding="utf-8") as f:          # 保存的样式：李毅-第1,2,3……页.html
            f.write(html_str)

    # 入口，调动者
    def run(self):
        '''实现主逻辑'''
        # 1. 构造url列表
        url_list = self.get_url_list()
        # 2. 遍历，发送请求，获取响应
        for url in url_list:
            html_str = self.parse_url(url)      # 响应的html字符串
        # 3. 保存
            # URL在当前url_list的位置
            page_name = url.list.index(url)+1   # 页码数
            self.save_html(html_str,page_name)


if __name__ == "__main__":
    # 实例化一个类 = 调用一个类
    tieba_spider = TiebaSpider("lol")
    tieba_spider.run()