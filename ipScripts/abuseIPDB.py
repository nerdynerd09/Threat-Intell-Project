import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()

def abuseIPDBFunc(ipValue):
    url = 'https://api.abuseipdb.com/api/v2/check'

    querystring = {
        'ipAddress': ipValue,
        'maxAgeInDays': '90'
    }

    headers = {
        'Accept': 'application/json',
        'Key': f'{os.getenv("ABUSE_IP_DB_API_KEY")}'
    }

    response = requests.request(method='GET', url=url, headers=headers, params=querystring)

    decodedResponse = json.loads(response.text)["data"]["abuseConfidenceScore"]
    return decodedResponse
