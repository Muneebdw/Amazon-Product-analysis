import requests
from bs4 import BeautifulSoup
import csv

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/90.0.4430.212 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
  

def get_html(url):
    r = requests.get(url, headers=HEADERS)
    print(r)
    return r.text

def soupify(html):
    return BeautifulSoup(html, 'html.parser')


def cus_data(soup):
    data_str = ""
    cus_list = []
  
    for item in soup.find_all("span", class_="a-profile-name"):
        data_str = data_str + item.get_text()
        cus_list.append(data_str)
        data_str = ""
    return cus_list

def rev_data(soup):
    data_str = ""
    rev_list = []
    for item in soup.find_all("span", class_="a-size-base review-text"):
        data_str = data_str + item.get_text()
        rev_list.append(data_str)
        data_str = ""
    return rev_list
url = 'https://www.amazon.com/MSI-Stealth-15M-Gaming-Laptop/dp/B091GGZT1S/ref=sr_1_1_sspa?crid=8SMPWBFYO1OF&keywords=gaming+laptop&qid=1657708306&smid=ATVPDKIKX0DER&sprefix=gaming%2Caps%2C471&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyR1NCVkZGRzRZMzI2JmVuY3J5cHRlZElkPUEwODA5NTQ1TjRaTlhLNldHSTNOJmVuY3J5cHRlZEFkSWQ9QTA5NDE1ODAyVUpTSzFFQzc2UFBMJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
data = get_html(url)
soup = soupify(data)

#scrape class a-profile-name
names = cus_data(soup)
reviews = rev_data(soup)

#Save Name + Review in csv
with open('reviews.csv', 'w' , encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Review'])
    for i in range(len(reviews)):
        writer.writerow([names[i+1], reviews[i]])

#convert csv to xlss
import pandas as pd
df = pd.read_csv('reviews.csv')
df.to_excel('reviews.xlsx', index=False)
