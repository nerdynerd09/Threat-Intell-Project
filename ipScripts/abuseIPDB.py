import requests
import json

# Defining the api-endpoint
url = 'https://api.abuseipdb.com/api/v2/check'

querystring = {
    # 'ipAddress': '118.25.6.39',
    'ipAddress': '65.49.20.67',
    'maxAgeInDays': '90'
}

headers = {
    'Accept': 'application/json',
    'Key': '6b7c386dd3f6274c74c8b30f19900199b8a5b8b62651ec13d55ade05c456c5d9c1f6c7b23b8dfb06'
}

response = requests.request(method='GET', url=url, headers=headers, params=querystring)

# Formatted output
decodedResponse = json.loads(response.text)["data"]["abuseConfidenceScore"]
print(decodedResponse)
# print (json.dumps(decodedResponse, sort_keys=True, indent=4))