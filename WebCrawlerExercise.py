import urllib.request
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import csv
with open("GENERATE.CSV", "w", newline="") as WCFILE:
    FileWriter = csv.writer(WCFILE)
    FileWriter.writerow(["URL", "HTMLPAGE TITLE", "HTTP Status Code"])


def web_crawler(max_pages):
    page = 1
    while page <= max_pages:
        url = 'http://www.tyre-shopper.co.uk/' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        sstatus_code = '200'
        r = requests.get(url)
        data = []
        for link in soup.findAll('a', {'class': ''}):
            href = link.get('href')
            title = link.string
            data.append([href, title, sstatus_code])
            ##print(href)
            ##print(title)
            ##print(r.json)
            print(href,'/',title,'/',sstatus_code)
            ##print(data)
            ##print("END OF CRWALING")
        page += 1
        with open("GENERATE.CSV", "a", newline="") as wcfile:
            FileWriter = csv.writer(wcfile, delimiter=',')
            for i in range(len(data)):
                FileWriter.writerows(data)
                data=i + 1
            FileWriter.close()
    FileWriter.close()
web_crawler(1)








