import requests
import json

# qyhxyw.com --red zone (dangerous)
# iprice.pl -- green zone (safe)
# www.xn--stelar-6db.com -- red zone(dangerous)
# remax.talkdrawer.com -- green zone (safe)
# sgs-gabon.com -- orange zone (not trusted)
# cfyfjvh.com --Grey zone (not listed yet)
# collaboratemedaltrips.com -- yellow zone (adware)

def kasperskyURL(urlValue):

    # if "://" in urlValue:
    #     urlValue  = urlValue.split("://")[1]
    #     print(urlValue)
    # else:
    #     urlValue = urlValue

    resultDict = {}
    headers = {
        'x-api-key': 'VraH95OsSSijV58XbPaAvA==',
    }

    response = requests.get(f'https://opentip.kaspersky.com/api/v1/search/domain?request={urlValue}', headers=headers)
    json_response=json.loads(response.text)
    print(json_response)

    url_zone=json_response['Zone']
    # print('Zone: '+ url_zone)
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
        # category_names=str(json_response['DomainGeneralInfo']['Categories'])
        # print(category_names)
        # print('URL Category:', str(category_names[0]))
    
    # resultDict['Zone'] = url_zone
    # resultDict['Category'] = category_names[0].split("_")[1]

    # print(resultDict)
    return resultDict

# kasperskyURL("collaboratemedaltrips.com")
# kasperskyURL("https://evil.com")
