"""
    需求：
        1. 使用link_text定位方式，使用注册A.html页面，点击 访问 新浪 网站 连接地址
    方法：
        1. driver.find_element_by_link_text("") # 定位元素方法
        2. click() # 点击方法
    注意：
        link_text：
            1. 只能定位a标签
            2. link_text定位元素的内容必须为全部匹配
"""

# 导包
from selenium import webdriver
from time import sleep


# 获取 浏览器驱动对象
driver = webdriver.Firefox()

# 打开 注册A.html
url = r"D:\web自动化素材\课堂素材\注册A.html"
driver.get(url)

# 使用 link_text定位 访问 新浪 网站 <全部匹配>
# driver.find_element_by_link_text("访问 新浪 网站").click()
# 错误写法，没有全部匹配文本
# driver.find_element_by_link_text("访问").click()

# 暂停 3秒
sleep(3)
# 退出浏览器驱动
driver.quit()
