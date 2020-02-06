# -*-coding:utf-8-*-
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/79.0.3945.88 Safari/537.36 "
}

url = "https://ac.qq.com/ComicView/index/id/505430/cid/1"

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)
# r = requests.get(url, headers = headers)
# r_str = r.content.decode()
# with open("onepiece.html", "w", encoding="utf-8") as f:
#     f.write(r_str)
driver.get(url)
element = driver.find_elements_by_xpath('//ul[@id="comicContain"]/li/img')
# element = driver.find_element_by_id("comicContain")
print(element)
print(driver.page_source)


time.sleep(5)
driver.quit()