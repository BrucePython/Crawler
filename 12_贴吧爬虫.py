# coding = utf-8
# 先设置start_url地址，把当前页的数据提取完后，再顺便提取下一页的url地址，再发起请求
# 详情页，从第一页开始，爬完后再爬取第二页……直到没有下一页为止
# ？提取当前页面的url地址总数？

import requests
from lxml import etree
import json

class TiebaSpider:
    def __init__(self,tieba_name):
        self.tieba_name = tieba_name
        # 获取的href不全，需要补齐
        '''
        self.part_url = "http://tieba.baidu.com/mo/q---1124EDCE0BAC22E4E6828666343D0508%3AFG%3D1--1-1-0--2--wapp_1527592885004_523/"
        self.start_url = "http://tieba.baidu.com/mo/q---1124EDCE0BAC22E4E6828666343D0508%3AFG%3D1--1-1-0--2--wapp_1527592885004_523/m?kw="+tieba_name+"&pn=0"
        self.headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
        '''
        self.start_url = "http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/m?kw=" + tieba_name + "&pn=0"
        self.part_url = "http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"}

    def parse_url(self,url):
        """发送请求，获取响应，url是变量"""
        print(url)
        response = requests.get(url, headers=self.headers)
        return  response.content

    def get_content_list(self, html_str):
        """提取数据"""
        html = etree.HTML(html_str)
        div_list = html.xpath("//div[contains(@class,'i')]")
        content_list = []               # 保存所有item，每一个item就是帖子的数据
        for div in div_list:
            item = {}
            # 由于xpath取出来的是列表，所以选取第1个值；只有长度大于0的时候，才能取值
            item["title"] = div.xpath("./a/text()")[0] if len(div.xpath("./a/text()")) > 0 else None
            # if 如果成立，则if前面的数据会传给变量，否则else的数据会传给变量
            item["href"] = self.part_url + div.xpath("./a/@href")[0] if len(div.xpath("./a/@href")) > 0 else None
            # 详情页的内容
            item["img_list"] = self.get_img_list(item["href"],[])   # 两个参数：detail_url和totle_img_list
            # 先unquote解码，按照src= 分割字符串，[-1]取后面的一部分
            item["img_list"] = [requests.utils.unquote(i).split("src=")[-1] for i in item["img_list"]]
            content_list.append(item)
        # 提取下一页的url地址(是列表) ---- 5. 请求下一页的url地址，进入循环2-5步
        next_url = self.part_url + html.xpath("//a[text()='下一页']/@href")[0] if len(html.xpath("//a[text()='下一页']/@href"))>0 else None
        return content_list, next_url

    def get_img_list(self,detail_url, total_img_list):
        """获取帖子的所有图片"""
        # （2）--请求列表页的url地址，获取详情页的第一页
        detail_html_str = self.parse_url(detail_url)
        detail_html = etree.HTML(detail_html_str)
        # （3）--提取详情页第一页的图片，
        img_list = detail_html.xpath("//img[@class='BDE_Image']/@src")
        total_img_list.extend(img_list)
        # （4）--提取下一页的地址, 请求详情页下一页的地址parse_url，进入循环（2）-（4）
        detail_next_url = detail_html.xpath("//a[text()='下一页']/@href")
        if len(detail_next_url) > 0:
            detail_next_url = self.part_url + detail_next_url[0]
            '''
            detail_html_str = self.parse_url(detail_next_url)
            detail_html = etree.HTML(detail_html_str)
            img_list = detail_html.xpath("//img[@class='BDE_Image']/@src")
            detail_next_url = detail_html.xpath("//a[text()='下一页']/@href")
            '''
            return self.get_img_list(detail_next_url, total_img_list)       # 一定要加上递归函数的出口return，否则就会显示None
        return total_img_list

    def save_content_list(self, content_list):
        """保存数据"""
        # 文件名随贴吧名的变化而变化
        file_path = self.tieba_name +".txt"
        with open(file_path,"a",encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content,ensure_ascii=False, indent=2))        # 为什么要转成json字符串
                f.write("\n")           # 每一个帖子之间换行
        print("保存成功")

    def run(self):
        """实现主要逻辑"""
        next_url = self.start_url
        while next_url is not None: # 当下一页为空，则到了最后一页
            # 1. 设置start_url
            # 2. 发送请求，获取响应
            html_str = self.parse_url(next_url)
            # 3. 提取数据，提取下一页的url地址 ***********
            #     一个递归就能解决所有详情页的提取，因为详情页的第一页与第二页的提取方式是一样的
            # （1）--提取列表页的url地址和标题
            # （2）--请求列表页的url地址，获取详情页的第一页
            # （3）--提取详情页第一页的图片，提取下一页的地址
            # （4）--请求详情页下一页的地址，进入循环（2）-（4）
            print("@@@@@@@@@@@@@@@@@@@@@")
            content_list, next_url = self.get_content_list(html_str)
            # 4. 保存数据
            print('!!!!!!!!!!!!!!!!!!!!!')
            self.save_content_list(content_list)
            print("@@@@@@@@@@@@@@@@@@@@@")
            # 5. 请求下一页的url地址，进入循环2-5步

if __name__ == '__main__':
    tieba_spider = TiebaSpider("gfriend")
    tieba_spider.run()