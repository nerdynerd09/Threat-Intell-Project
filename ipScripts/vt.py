import requests 
import json
# ip_add='103.186.28.56' #malicious
ip_add='223.8.213.228' #malicious
# ip_add='107.178.17.33' # not malicious
# ip_add='216.58.194.174' #not malicious 
# ip_add='185.255.81.2'

def checkIP(ip_add):
    malicious_ip=[]
    url = "https://www.virustotal.com/api/v3/ip_addresses/"+ip_add

    headers = {
        "accept": "application/json",
        "x-apikey": "3dc154ab7a3998f30c0109a316def01db2576e6f8d37daa11ee768be5257b134"
    }

    response = requests.get(url, headers=headers)
    json_response=json.loads(response.text)
    # url_info = json_response['data']['attributes']['last_analysis_stats']['malicious']

    url_info = json_response['data']['attributes']['last_analysis_stats']
    print(url_info)
    return url_info
    # if url_info > 0:
    #     malicious_ip.append(ip_add)
    # else:
    #     malicious_ip.append("not malicious")

    # print(malicious_ip)




def checkURL(targetUrl):
    resultList = []

    url = "https://www.virustotal.com/api/v3/urls"

    payload = { "url": targetUrl }
    headers = {
        "accept": "application/json",
        "x-apikey": "3dc154ab7a3998f30c0109a316def01db2576e6f8d37daa11ee768be5257b134",
        "content-type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url, data=payload, headers=headers)
    # print(response.text)
        
    json_response = response.json()

    response2 = requests.get(json_response["data"]["links"]["self"],headers=headers)
    # print(response2.json()["data"]["attributes"]["stats"]["malicious"])
    # print(len(response2.json()["data"]["attributes"]["results"]))

    # resultList.append([response2.json()["data"]["attributes"]["stats"]["malicious"],len(response2.json()["data"]["attributes"]["results"])])
    # return resultList
    return(response2.json()["data"]["attributes"]["stats"])

# checkURL("https://evil.com/")
# checkURL("https://term.m4tt72.com/")
# checkURL("https://google.com/")

