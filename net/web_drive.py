#!/bin/python3
"""
webdriver访问网站页面，模拟点击事件
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def get_web_clicked_source(url, btn: list = []) -> str:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    element_all = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((
            By.XPATH,
            '//div[@class="b-btn playlist-pic-text__expand b-btn--round" and contains(text(), "全部")]'
        )))
    element_all.click()
    driver.implicitly_wait(10)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    result_episode_list = soup.find_all('div', class_='layout-main')
    if result_episode_list:
        for episode in result_episode_list:
            print(str(episode))
    driver.quit()
    return page_source
