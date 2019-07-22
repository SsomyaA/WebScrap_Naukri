from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
from xlsxwriter import Workbook
import xlrd

driver = webdriver.Chrome('/Users/somyabiswal/Documents/BeutifulSoup/chromedriver')
main_url = "https://www.naukri.com/data-analyst-jobs-in-bangalore"
# driver.get(main_url)

post_url = []


for i in range(1, 19):

    if i == 1:
        print(main_url)
        driver.get(main_url)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        url = soup.find_all("div", attrs= {"type": "tuple"})
        opening_url = [link["data-url"] for link in url]
        # sleep(2)
        post_url = post_url + opening_url
        # sleep(2)

    else:
        main_url = "https://www.naukri.com/data-analyst-jobs-in-bangalore" + "-" + str(i) + "/"
        print(main_url)

        driver.get(main_url)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        url = soup.find_all("div", attrs= {"type": "tuple"})
        opening_url = [link["data-url"] for link in url]
        # sleep(2)
        print(opening_url)
        post_url = post_url + opening_url
        # sleep(2)



print(len(post_url))