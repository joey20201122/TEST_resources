# 导包
from selenium import webdriver
from time import sleep
# 获取浏览器驱动对象
driver = webdriver.Firefox()

# 打开url
url = r"D:\web自动化素材\课堂素材\注册A.html"
driver.get(url)
# 错误的实现
# driver.find_element_by_css_selector("[name='upfilea']").click()
# 正确实现，使用 send_keys("文件路径及文件名")
driver.find_element_by_css_selector("[name='upfilea']").send_keys("D:\hello123.txt")


# 暂停 2
sleep(2)
# 关闭驱动对象
driver.quit()