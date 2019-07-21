from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
from xlsxwriter import Workbook
import xlrd

# Setting-Up User-Agent
ua = UserAgent()
header = {'user-agent': ua.chrome}

scrape_page = requests.get("https://www.naukri.com/data-analyst-jobs-in-bangalore", headers = header)
