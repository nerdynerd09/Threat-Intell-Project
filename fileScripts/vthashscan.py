import requests

def VT_Request(hash):
        
        key = '3dc154ab7a3998f30c0109a316def01db2576e6f8d37daa11ee768be5257b134'

        params = {'apikey': key, 'resource': hash}
        url = requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=params)
        json_response = url.json()
        response = int(json_response.get('response_code'))
        if response == 0:
                return ('Non malicious')
        elif response == 1:
                positives = int(json_response.get('positives'))
                if positives == 0:
                        return ('Non malicious')
                else:
                        return ('Malicious')
        else:
                return ('Non malicious')

# def main():
#         # hashInput='c0202cf6aeab8437c638533d14563d35' #malicious hash
#         # hasInput='2d75cc1bf8e57872781f9cd04a529256'  #malicious hash
        
#         hashInput= input("Enter the hash of the file:")
#         # print(hashInput)
#         if len(hashInput) == 32:
#             hashInput = hashInput
#         elif len(hashInput) == 40:
#             hashInput = hashInput
#         elif len(hashInput) == 64:
#             hashInput = hashInput
#         else:
#             print ("The Hash input does not appear valid.")
#             exit()
#         VT_Request(key, hashInput)                                                                                                                                                                           
                                                                                                                                                                                                                                           

# running the program
# if __name__ == '__main__':
#         main()

# print(VT_Request("2d75cc1bf8e57872781f9cd04a52emf56"))