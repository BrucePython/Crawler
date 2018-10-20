# coding:utf-8

# 可用于登陆，登陆就是为了获取cookie

from selenium import webdriver
import time

# 实例化一个浏览器
driver = webdriver.Chrome()

# 设置窗口大小
# driver.set_window_size(1920,1080)
# 最大化窗口
driver.maximize_window()

# 1. 加载页面：发送请求，弹出浏览器
driver.get("https://www.baidu.com")

# 页面截屏
driver.save_screenshot("./baidu.png")

# 2.元素定位的方法，并发送内容
driver.find_element_by_id("kw").send_keys("Python")
driver.find_element_by_id("su").click()

# 3. 查看请求信息
# 3.1 driver获取cookie, get_cookies可获得当前driver里面的所有cookie
cookies = driver.get_cookies()  # 输出的是列表型的cookie，每一个元素就是一条cookie字典
"""
[{'domain': '.baidu.com', 'httpOnly': False, 'name': 'H_PS_PSSID', 'path': '/', 'secure': False, 'value': '26523_1460_21103_26350_20928'}, 
 {'domain': '.baidu.com', 'expiry': 3675170902.158308, 'httpOnly': False, 'name': 'BIDUPSID', 'path': '/', 'secure': False, 'value': '1215B01DA2EB119EF66F6D00468F8E1B'}, 
 {'domain': '.baidu.com', 'expiry': 3675170902.158362, 'httpOnly': False, 'name': 'PSTM', 'path': '/', 'secure': False, 'value': '1527687254'}, 
 {'domain': 'www.baidu.com', 'expiry': 1528551258, 'httpOnly': False, 'name': 'BD_UPN', 'path': '/', 'secure': False, 'value': '123253'}, 
 {'domain': 'www.baidu.com', 'httpOnly': False, 'name': 'BD_HOME', 'path': '/', 'secure': False, 'value': '0'}, 
 {'domain': '.baidu.com', 'expiry': 3675170902.158186, 'httpOnly': False, 'name': 'BAIDUID', 'path': '/', 'secure': False, 'value': '1215B01DA2EB119EF66F6D00468F8E1B:FG=1'}]

{'H_PS_PSSID': '1444_21122_26430', 'BIDUPSID': '8B0ABFEFBB2F6214A81D67C999CC8A12', 'PSTM': '1527687143', 'BD_UPN': '123253', 'BD_HOME': '0', 'BAIDUID': '8B0ABFEFBB2F6214A81D67C999CC8A12:FG=1'}
"""

# 转化成request能用的cookie字典: 键值对
cookies = {i["name"]: i["value"] for i in cookies}
print(cookies)


# 3.2 driver获取html字符串，elements的内容，因为driver本身就是浏览器，已经执行了js和css
# print(driver.page_source)

# 3.3
print(driver.current_url) # click之后的url地址

# 4. 退出
# 退出当前页面
driver.close()
time.sleep(3)
# 退出浏览器
driver.quit()
