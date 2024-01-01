import requests
from dotenv import load_dotenv
import os
load_dotenv()

def VT_Request(hash):
        resultDict = {}    
        key = os.getenv("VIRUSTOTAL_API")
        params = {'apikey': key, 'resource': hash}
        url = requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=params)
        json_response = url.json()
        response = int(json_response.get('response_code'))
        if response == 0:
                resultDict["Status"] = "Safe"
        elif response == 1:
                positives = int(json_response.get('positives'))
                if positives == 0:
                        resultDict["Status"] = "Safe"
                else:
                        resultDict["Status"] = "Malicious"
        else:
                resultDict["Status"] = "Safe"
        
        return resultDict

