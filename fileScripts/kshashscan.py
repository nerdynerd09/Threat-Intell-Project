import requests
import json

# red zone - A5085E571857EC54CF9625050DFC29A195DAD4D52BEA9B69D3F22E33ED636525
# yellow zone - A616FC2C1A075170D4DECDB9D3C9AD15F2CFBCFDA78DBE4C60D72132B9D006C9
# green zone - F4408BAA3CE59B7D184B46A37D660D44D4F7EBA746B76B9159B4C358C980C07C

def kasperskyHash(hashValue):
    headers = {
        'x-api-key': 'VraH95OsSSijV58XbPaAvA==',
    }

    resultDict = {}
    try:
        response = requests.get(f'https://opentip.kaspersky.com/api/v1/search/hash?request={hashValue}', headers=headers)
        json_response = json.loads(response.text)
        hash_zone = json_response['Zone']
        detection_names = []

        if (hash_zone == 'Red' or hash_zone == 'Yellow' or hash_zone == 'Orange'):
            try:
                for detection_info in json_response['DetectionsInfo']:
                    detection_names.append(detection_info['DetectionName'])
            # print(f"Detected as: {', '.join(detection_names)}")
            # print(detection_names)
            except Exception as e:
                category_names = [""]

            resultDict["Status"] = "Malicious"

        elif json_response["Zone"] == "Green":
            resultDict["Status"] = "Safe"

        elif json_response["Zone"] == "Grey":
            resultDict["Status"] = "Untrusted"

    except Exception as e:
        resultDict["Status"] = "Undefined"

    # print(resultDict)
    return resultDict

# kasperskyHash('A5085E571857EC54CF9625050DFC29A195DAD4D52BEA9B69D3F22E33ED636525')
# kasperskyHash('A616FC2C1A075170D4DECDB9D3C9AD15F2CFBCFDA78DBE4C60D72132B9D006C9')
# kasperskyHash('F4408BAA3CE59B7D184B46A37D660D44D4F7EBA746B76B9159B4C358C980C07C')
# kasperskyHash('f99334198c0ce814b8c95e88c540aac21aabd9f00b89dbf29f207f27fa4d4292')