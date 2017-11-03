#coding=utf-8 
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
# 用get打开百度页面
driver.get("http://www.baidu.com")
# 查找页面的“设置”选项，并进行点击
sleep(1)
driver.find_elements_by_link_text('设置')[0].click()
# 打开设置后找到“搜索设置”选项，设置为每页显示50条
driver.find_elements_by_link_text('搜索设置')[0].click()
m = driver.find_element_by_id("nr")
sleep(2)
m.find_element_by_xpath('//*[@id="nr"]/option[3]').click()
sleep(2)
# 处理弹出的警告页面
driver.find_element_by_class_name("prefpanelgo").click()
sleep(2)
driver.switch_to_alert().accept()
sleep(2)
# 找到百度的输入框，并输入“selenium”
keywords = 'selenium'
send_keywords = keywords.decode('utf-8')
driver.find_element_by_id("kw").send_keys(send_keywords)
sleep(2)
# 点击搜索按钮
driver.find_element_by_xpath("//*[@id='su']").click()
sleep(2)
# 在打开的页面中找到“selenium－开源中国社区”，并打开这个页面
driver.find_elements_by_link_text('功能自动化测试工具——Selenium篇')[0].click()
