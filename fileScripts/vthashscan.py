import requests
key = '3dc154ab7a3998f30c0109a316def01db2576e6f8d37daa11ee768be5257b134'

def VT_Request(key, hash):
        params = {'apikey': key, 'resource': hash}
        url = requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=params)
        json_response = url.json()
        response = int(json_response.get('response_code'))
        if response == 0:
                print ( hash + ' is not in Virus Total')
        elif response == 1:
                positives = int(json_response.get('positives'))
                if positives == 0:
                        print (hash + ' is not malicious')
                else:
                        print ( hash + ' is malicious')
        else:
                print (hash + ' could not be searched. Please try again later.')

def main():
        # hashInput='c0202cf6aeab8437c638533d14563d35' #malicious hash
        # hasInput='2d75cc1bf8e57872781f9cd04a529256'  #malicious hash
        
        hashInput= input("Enter the hash of the file:")
        # print(hashInput)
        if len(hashInput) == 32:
            hashInput = hashInput
        elif len(hashInput) == 40:
            hashInput = hashInput
        elif len(hashInput) == 64:
            hashInput = hashInput
        else:
            print ("The Hash input does not appear valid.")
            exit()
        VT_Request(key, hashInput)                                                                                                                                                                           
                                                                                                                                                                                                                                           

# running the program
if __name__ == '__main__':
        main()