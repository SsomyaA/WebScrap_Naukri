from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
from xlsxwriter import Workbook
import xlrd


driver = webdriver.Chrome('/Users/somyabiswal/Documents/BeutifulSoup/chromedriver')
# main_url = "https://www.naukri.com/job-listings-Senior-Data-Scientist-Peopleplus-Professional-Services-Pvt-Ltd-Bengaluru-4-to-7-years-280619502158?src=jobsearchDesk&sid=15637883955475&xp=1&px=17"
main_url = "https://www.naukri.com/job-listings-Tracxn-BD-Manager-EMEA-Customer-Support-exp-Preferred-5-9-yrs-Tracxn-Technologies-Pvt-Ltd-Bengaluru-5-to-9-years-150719009908?src=rcntSrchWithCount&sid=1563822904665&xp=1&px=1"

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

if url2[0] is not None:
    salary = url2[0].text


# URL3

url3 = soup1.find_all("div", attrs= {"class": "sumFoot"})

openings_no = url3[0].span.next_sibling.next_sibling.next_sibling.next_sibling.strong.text
posting_date = url3[0].span.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text
number_of_applicant = url3[0].span.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.strong.text
number_of_view = url3[0].span.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.strong.text

print(profile_name)
print(position)
print(exp_year)
print(location)
print(salary)
print(openings_no)
print(posting_date)
print(number_of_applicant)
print(number_of_view)

# URL4

url4 = soup1.find_all("div", attrs= {"class": "jDisc mt20"})

industry = url4[0].p.next_sibling.next_sibling.span.text
functional_area = url4[0].p.next_sibling.next_sibling.next_sibling.next_sibling.span.text
role_category = url4[0].p.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.span.text
role = url4[0].p.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.span.text
employment_type = url4[0].p.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.span.text

# URL5

url5 = soup1.find_all("font", attrs= {"class": "hlite"})

skills = []
for skill in range(len(url5)):
    skills.append(url5[skill].text)


print(industry)
print(functional_area)
print(role_category)
print(role)
print(employment_type)
print(skills)