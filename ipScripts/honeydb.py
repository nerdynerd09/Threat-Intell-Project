import requests,json
from dotenv import load_dotenv
import os
load_dotenv()

def honeyDB(ipValue):
    headers = {
        'X-HoneyDb-ApiId': f'{os.getenv("HONEY_DB_API_ID")}',
        'X-HoneyDb-ApiKey': f'{os.getenv("HONEY_DB_API_KEY")}',
    }

    response = requests.get(f'https://honeydb.io/api/ipinfo/{ipValue}', headers=headers)

    if json.loads(response.text)["is_threat"] == True:
        result = "Malicious"
    else:
        result = "Safe"

    return result

