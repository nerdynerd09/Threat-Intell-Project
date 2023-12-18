import pymongo
import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8'] 

uri = "mongodb+srv://viaathreatintel:rrDsKYeblTyDitLK@cluster0.mckr9yr.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
myclient = pymongo.MongoClient(uri)
mydb = myclient["iitk"]
mycol = mydb["threatintell"]
mycol1 = mydb["CountofSearches"]

def dbAtlas():
    print((mycol.count_documents({})))

def dbIPStore(resultList):
    # print(result)
    for i in resultList:
        if mycol.find_one({"ip":i[0]}) is None:
            mycol.insert_one({"ip":i[0],"location":i[1]})

def dbHashStore(resultList,pageNumber):
    # print(result)
    for i in resultList:
        if mycol.find_one({"hash":i}) is None:
            mycol.insert_one({"hash":i})
        
    print(f"Data inserted for page number: {pageNumber}")

def dbHashSearch(hashValue):
    if mycol.find_one({"hash":hashValue}) is None:
        return "Safe"
    else:
        return "Malicious"

def dbSearch(target):
    if mycol.find_one({"ip":target}) is None:
        return "Non-malicious IP"
    else:
        return "Malicious IP"
    
def SearchIPCount(): #to store the count of total IP Searches in the Database and retrieving the same.
    result = mycol1.find_one({})
    mycol1.update_one({}, {"$inc": {"ipsearchcount": 1}}, upsert=True)
    searchedIP = result.get("ipsearchcount", 0)
    #print(f"Number of IP Searches: {searchedIP}")
    return searchedIP
    
def dbURLSearch(target):
    if mycol.find_one({"url":target}) is None:
        return "Safe"
    else:
        return "Malicious"
    
def SearchURLCount(): #to store the count of total URL Searches in the Database and retrieving the same.
    result = mycol1.find_one({})
    mycol1.update_one({}, {"$inc": {"urlsearchcount": 1}}, upsert=True)
    searchedURL = result.get("urlsearchcount", 0)
    #print(f"Number of IP Searches: {searchedURL}")
    return searchedURL
    
def countdbIPAddresses(): #to count total number of IPs stored in the database
    count_totalIpAddresses = mycol.count_documents({"ip": {"$exists": True}})
    print(f"Number of IP addresses in the database: {count_totalIpAddresses}")
    return count_totalIpAddresses

def countdbhashValues(): #to count total number of hashvalues stored in the database
    count_totalhashValues = mycol.count_documents({"hash": {"$exists": True}})
    print(f"Number of hash values in the database: {count_totalhashValues}")
    return count_totalhashValues

def countdbUrls(): #to count total number of urls stored in the database
    count_totalUrls = mycol.count_documents({"url": {"$exists": True}})
    print(f"Number of urls in the database: {count_totalUrls}")
    return count_totalUrls

# dbAtlas()

def fileScanResult(hashValue,result):
   
    fileHashCol = mydb["fileScanResult"]
   
    if fileHashCol.find_one({"hash":hashValue}):
        resultDict = fileHashCol.find_one({"hash":hashValue})["result"]
        resultDict[list(result.keys())[0]] = list(result.values())[0]

        fileHashCol.update_one({"hash":hashValue},{"$set":{"result":resultDict}})
    else:
        fileHashCol.insert_one({"hash":hashValue,"result":result})


countdbIPAddresses()
countdbhashValues()
countdbUrls()
