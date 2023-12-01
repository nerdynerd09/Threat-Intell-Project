import requests
import json

# 51.38.81.65 --red zone (dangerous)
# 95.156.121.11 -- green zone (safe)
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
    # print(json_response)
    ip_zone=json_response['Zone']
    print('Zone: '+ ip_zone)
    if(ip_zone=='Red' or ip_zone == 'Orange' or ip_zone=='Yellow'):
        categories_with_zone = (json_response['IpGeneralInfo']['CategoriesWithZone'])
        category_names = [category['Name'] for category in categories_with_zone]
        # category_names=str(json_response['IpGeneralInfo']['Categories'])
        print('IP Category:', category_names[0])
        resultDict["Zone"] = json_response['Zone']
        resultDict["Category"] = category_names[0]
        # print(resultDict)
        # resultList.append([json_response['Zone'],category_names[0]])
    return resultDict

# kasperskyIP("51.38.81.65")