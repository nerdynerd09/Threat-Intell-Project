import requests
import json

# red zone - A5085E571857EC54CF9625050DFC29A195DAD4D52BEA9B69D3F22E33ED636525
# yellow zone - A616FC2C1A075170D4DECDB9D3C9AD15F2CFBCFDA78DBE4C60D72132B9D006C9
# green zone - F4408BAA3CE59B7D184B46A37D660D44D4F7EBA746B76B9159B4C358C980C07C

headers = {
    'x-api-key': 'VraH95OsSSijV58XbPaAvA==',
}

response = requests.get('https://opentip.kaspersky.com/api/v1/search/hash?request=A5085E571857EC54CF9625050DFC29A195DAD4D52BEA9B69D3F22E33ED636525', headers=headers)

json_response = json.loads(response.text)
print(response.text)
print(json_response)

hash_zone = json_response['Zone']
print("Zone: " + hash_zone)
detection_names = []

if (hash_zone == 'Red' or hash_zone == 'Yellow' or hash_zone == 'Orange'):
    for detection_info in json_response['DetectionsInfo']:
        detection_names.append(detection_info['DetectionName'])
    print(f"Detected as: {', '.join(detection_names)}")