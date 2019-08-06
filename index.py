from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
from xlsxwriter import Workbook
import xlrd

Wb = Workbook('scrap_filee.xlsx')
Sh  = Wb.add_worksheet()

driver = webdriver.Chrome('/Users/somyabiswal/Documents/BeutifulSoup/chromedriver')
main_url = "https://www.naukri.com/data-analyst-jobs-in-bangalore"
# driver.get(main_url)

post_url = []

excel_array = []

misssed_domain = 0
counter = 0

for i in range(9, 19):

    if i == 1:
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
        # print(opening_url)
        post_url = post_url + opening_url
        # sleep(2)


total_url = len(post_url)
print(total_url)

for each_url in post_url:
    main_url = each_url

    driver.get(main_url)
    soup1 = BeautifulSoup(driver.page_source, 'lxml')

    try:

        counter = counter + 1

        # # Adding New excel Workbook
        # if counter % 3 == 0:
        #     pass
        # else:
        #     pass

        # URL1
        url1 = soup1.find_all("div", attrs={"class": "hdSec"})
        print(main_url)
        profile_name = url1[0].h1.text
        position = url1[0].div.text
        exp_year = url1[0].div.next_sibling.next_sibling.text
        location = url1[0].div.next_sibling.next_sibling.next_sibling.next_sibling.text

        # URL2
        url2 = soup1.find_all("span", attrs={"class": "sal"})

        if url2[0] is not None:
            salary = url2[0].text

        # URL3

        url3 = soup1.find_all("div", attrs={"class": "sumFoot"})

        openings_no = url3[0].span.next_sibling.next_sibling.next_sibling.next_sibling.strong.text
        posting_date = url3[0].span.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text
        number_of_applicant = url3[
            0].span.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.strong.text
        number_of_view = url3[
            0].span.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.strong.text



        # URL4

        url4 = soup1.find_all("div", attrs={"class": "jDisc mt20"})

        industry = url4[0].p.next_sibling.next_sibling.span.text
        functional_area = url4[0].p.next_sibling.next_sibling.next_sibling.next_sibling.span.text
        role_category = url4[0].p.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.span.text
        role = url4[
            0].p.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.span.text
        employment_type = url4[
            0].p.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.span.text

        # URL5

        url5 = soup1.find_all("font", attrs={"class": "hlite"})

        skills = []
        for skill in range(len(url5)):
            skills.append(url5[skill].text)


        def convert(list):
            res = str(",".join(map(str, list)))
            return res

        my_skill = convert(skills)


        # Adding 1st 50 elements into an array

        each_opening_array = [profile_name, position, exp_year, location, salary, openings_no, posting_date, number_of_applicant,number_of_view, industry, functional_area, role_category, role, employment_type, my_skill]


        excel_array.append(each_opening_array)





    except:
        misssed_domain = misssed_domain +1

# print(excel_array)

rows = len(excel_array)
print(rows)

for row in range(rows):
    Sh.write_row(row, 0, excel_array[row])
    print("banda")


Wb.close()
