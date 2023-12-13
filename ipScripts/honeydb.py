import requests,json

def honeyDB(ipValue):
    headers = {
        'X-HoneyDb-ApiId': 'e502f401daa54ad671880d5324f461aa9e0c6f3c6aeaccc203a7522a13efe560',
        'X-HoneyDb-ApiKey': 'a4032c383b2ac2b374524f0fb150b4081c1c738a9834f586a20ccec18fef090b',
    }

    response = requests.get(f'https://honeydb.io/api/ipinfo/{ipValue}', headers=headers)

    if json.loads(response.text)["is_threat"] == True:
        result = "Malicious"
    else:
        result = "Safe"

    return result


# ip = "65.49.20.67"
# ip = "218.92.0.208"
# honeyDB(ip)