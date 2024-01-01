import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()

def kasperskyIP(ipValue):
    resultDict = {}

    headers = {
        'x-api-key': f'{os.getenv("KASPERSKY_API_TOKEN")}',
    }

    response = requests.get(f'https://opentip.kaspersky.com/api/v1/search/ip?request={ipValue}', headers=headers)
    json_response=json.loads(response.text)
    
    print(response.text)
    if json_response["Zone"] == "Red" or json_response["Zone"]=="Orange" or json_response["Zone"]=="Yellow":
        try:
            categories_with_zone = (json_response['IpGeneralInfo']['CategoriesWithZone'])
            category_names = [category['Name'] for category in categories_with_zone]
            resultDict["Category"] = category_names[0].split("_")[1]
        except Exception as e:
            category_names = [""]

        resultDict["Status"] = "Malicious"
    
    elif json_response["Zone"] == "Green":
        resultDict["Status"] = "Safe"

    elif json_response["Zone"] == "Grey":
        resultDict["Status"] = "Untrusted"

    print(resultDict)
    return resultDict

# kasperskyIP("95.156.121.11")