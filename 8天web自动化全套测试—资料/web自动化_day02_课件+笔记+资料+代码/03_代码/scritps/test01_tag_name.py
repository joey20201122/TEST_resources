"""
    需求：
        1. 使用tag_name定位方式，使用注册A.html页面，用户名输入admin
    方法：
        1. driver.find_element_by_tag_name("") # 定位元素方法
        2. send_keys() # 输入方法
        3. driver.quit() # 退出方法
"""

# 导包
from selenium import webdriver
from time import sleep


# 获取 浏览器驱动对象
driver = webdriver.Firefox()

# 打开 注册A.html
url = r"D:\web自动化素材\课堂素材\注册A.html"
driver.get(url)

# 使用tag_name定位用户名 并 输入admin
# 注意：页面中如果存在多个相同的标签名，默认返回第一个标签
driver.find_element_by_tag_name("input").send_keys("admin")

# 暂停 3秒
sleep(3)
# 退出浏览器驱动
driver.quit()
