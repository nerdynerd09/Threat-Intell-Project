import requests
import json

# 51.38.81.65 --red zone (dangerous)
# 95.156.121.11 --green zone (safe)
# 2.179.195.10 -- orange zone (not trusted)
# 223.8.213.228--Grey zone (not listed yet)

def kasperskyIP(ipValue):
    resultList = []
    resultDict = {}
    headers = {
        'x-api-key': 'VraH95OsSSijV58XbPaAvA==',
    }

    response = requests.get(f'https://opentip.kaspersky.com/api/v1/search/ip?request={ipValue}', headers=headers)
    json_response=json.loads(response.text)
    

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

# kasperskyIP("51.38.81.65")
# kasperskyIP("95.156.121.11")
# kasperskyIP("223.8.213.228")