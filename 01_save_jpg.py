import requests

# 发送请求
response = requests.get("https://www.baidu.com/img/bd_logo1.png")
# wb: 视频 音频 图片 pdf
# w: html界面

# 保存
with open("./baidu.png", "wb") as f:
    f.write(response.content)
    # f.write(response.content.decode())

