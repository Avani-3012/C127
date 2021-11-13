from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
STARTURL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("chromedriver.exe")
browser.get(STARTURL)
time.sleep(10)
headers = ["name", "distance", "mass", "radius"]
star_data = []

def scrapedata():
    soup = BeautifulSoup(browser.page_source, "html.parser")
    table =soup.find('table')
    table_rows = table[7].find_all('tr')
    for tr_tag in table:
        td_tags = tr_tag.find("td")
        temp_list = []
        for td_tag in td_tags:
            temp_list.append(td_tag.text.rstrip())
        star_data.append(temp_list)
        
    with open("scrapper.csv", "w") as a:
        csvwriter = csv.writer(a)
        csvwriter.writerow(headers)
        csvwriter.writerows(star_data)
scrapedata()