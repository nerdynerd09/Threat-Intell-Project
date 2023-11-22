# https://www.socinvestigation.com/category/ioc/
# https://www.socinvestigation.com/category/ioc/page/2/

import requests
from bs4 import BeautifulSoup

def latestIoC():
    url = "https://www.socinvestigation.com/category/ioc/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"lxml")

    anchorTags = soup.find_all(class_="td-module-title")
    newsLinkList = []

    for i in anchorTags:
        newsLinkList.append([i.find('a').text.strip(),i.find('a').get('href')])

    return newsLinkList
