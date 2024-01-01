import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()

def kasperskyURL(urlValue):

    if "://" in urlValue:
        urlValue  = urlValue.split("://")[1]
        print(urlValue)
    else:
        urlValue = urlValue

    resultDict = {}
    headers = {
        'x-api-key': f'{os.getenv("KASPERSKY_API_TOKEN")}',
    }

    response = requests.get(f'https://opentip.kaspersky.com/api/v1/search/domain?request={urlValue}', headers=headers)
    json_response=json.loads(response.text)

    url_zone=json_response['Zone']
    if(url_zone=='Red' or url_zone == 'Orange' or url_zone=='Yellow'):
        try:
            categories_with_zone = (json_response['DomainGeneralInfo']['CategoriesWithZone'])
            category_names = [category['Name'] for category in categories_with_zone]
        except Exception as e:
            category_names = [""]

        resultDict["Status"] = "Malicious"
    
    elif json_response["Zone"] == "Green":
        resultDict["Status"] = "Safe"

    elif json_response["Zone"] == "Grey":
        resultDict["Status"] = "Untrusted"

    return resultDict


