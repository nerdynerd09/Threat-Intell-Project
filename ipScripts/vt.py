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

    return url_info
    # if url_info > 0:
    #     malicious_ip.append(ip_add)
    # else:
    #     malicious_ip.append("not malicious")

    # print(malicious_ip)




def checkURL(url):
    malicious_url = []
    url_vt = "https://www.virustotal.com/api/v3/urls/" + url

    headers = {
        "x-apikey": "3dc154ab7a3998f30c0109a316def01db2576e6f8d37daa11ee768be5257b134"
    }

    response = requests.get(url_vt, headers=headers)
    json_response = response.json()

    try:
        last_analysis_stats = json_response['data']['attributes']['last_analysis_stats']
        if 'malicious' in last_analysis_stats and last_analysis_stats['malicious'] > 0:
            malicious_url.append(url)
    except KeyError:
        # Handle the case where 'data' key is not present in the response
        return {"error": "Invalid response format"}

    return malicious_url
    # print(malicious_url)

