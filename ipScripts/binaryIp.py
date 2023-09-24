import requests
import re
from bs4 import BeautifulSoup
from dbFile import dbStore


def binaryIPCollector():

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    url = "https://www.binarydefense.com/banlist.txt"

    resp = requests.get(url, headers=headers)
    bsContent = BeautifulSoup(resp.text, "lxml")
    # print(bsContent)

    result = re.findall(r'[0-9].*', str(bsContent))
    resultList = [[i, "NA"] for i in result]
    # print(resultList)

    dbStore(resultList=resultList)
    print("Done")
binaryIPCollector()