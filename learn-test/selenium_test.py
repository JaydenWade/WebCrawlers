# -*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
# instantiation a browser
# driver = webdriver.Chrome()
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)
# driver = webdriver.PhantomJS() now selenium was not support phantomjs,use the headless version of chrome or firefox

# set a request
driver.get("http://www.baidu.com")
# print(driver.title)
driver.save_screenshot("./baidu.png")

# positioning element
# driver.find_element_by_id("kw").send_keys("python")
# driver.find_element_by_id("su").click()

# quit browser
time.sleep(5)
driver.quit()