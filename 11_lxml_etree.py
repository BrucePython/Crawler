# lxml可自动修正代码，但有时候也会修正错了：
# 解决办法，使用etree.tostring观察修改之后的html的样子，根据修改之后的html字符串写xpath

# coding=utf-8
from lxml import etree

text1 = ''' <div> <ul> 
        <li class="item-1"><a href="link1.html">first item</a></li> 
        <li class="item-1"><a href="link2.html">second item</a></li> 
        <li class="item-inactive"><a href="link3.html">third item</a></li> 
        <li class="item-1"><a href="link4.html">fourth item</a></li> 
        <li class="item-0"><a href="link5.html">fifth item</a>  
        </ul> </div> '''

# 不对应：{'href': 'link2.html', 'title': 'first item'}，{'href': 'link4.html', 'title': 'second item'}
text = ''' <div> <ul> 
        <li class="item-1"><a>first item</a></li> 
        <li class="item-1"><a href="link2.html">second item</a></li> 
        <li class="item-inactive"><a href="link3.html">third item</a></li> 
        <li class="item-1"><a href="link4.html">fourth item</a></li> 
        <li class="item-0"><a href="link5.html">fifth item</a>  
        </ul> </div> '''

html = etree.HTML(text)
print(html)  # 获得element对象，可使用xpath方法

# 查看element中包含的字符串
# print(etree.tostring(html).decode())

# 获取class为itme-1 li下的a的href
ret1 = html.xpath("//li[@class='item-1']/a/@href")
print(ret1)

# 获取class为itme-1 li下的a的文本
ret2 = html.xpath("//li[@class='item-1']/a/text()")
print(ret2)

# 每个li是一条新闻，把url和文本组成字典
for href in ret1:
    item = {}
    item["href"] = href
    item["title"] = ret2[ret1.index(href)]  # ret1.index(href)：获取下标1，2，3……
    print(item)
print("*" * 20)

ret3 = html.xpath("//li[@class='item-1']")  # ret3 列表类型，列表里是element对象，可使用xpath方法

# 根据li标签进行分组，对每一组继续写xpath
for i in ret3:
    item = {}
    # . 当前节点为li标签；列表类型，因为有三个li元素；[0]: 取出每个列表第一个元素，并做判断
    item["title"] = i.xpath("./a/text()")[0] if len(i.xpath("./a/text()"))>0 else None
    item["href"] = i.xpath("./a/@href")[0] if len(i.xpath("./a/@href"))>0 else None
    print(item)
