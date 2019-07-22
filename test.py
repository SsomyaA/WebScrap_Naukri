from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
from xlsxwriter import Workbook
import xlrd


driver = webdriver.Chrome('/Users/somyabiswal/Documents/BeutifulSoup/chromedriver')
main_url = "https://www.naukri.com/job-listings-Senior-Data-Scientist-Peopleplus-Professional-Services-Pvt-Ltd-Bengaluru-4-to-7-years-280619502158?src=jobsearchDesk&sid=15637883955475&xp=1&px=17"

driver.get(main_url)
soup1 = BeautifulSoup(driver.page_source, 'lxml')

# URL1
url1 = soup1.find_all("div", attrs= {"class": "hdSec"})

profile_name = url1[0].h1.text
position = url1[0].div.text
exp_year = print(url1[0].div.next_sibling.next_sibling.text)
location = url1[0].div.next_sibling.next_sibling.next_sibling.next_sibling.text

# URL2
url2 = soup1.find_all("span", attrs= {"class": "sal"})

if url2 is not None:
    salary = k.text