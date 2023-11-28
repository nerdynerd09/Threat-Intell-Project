import pymongo
import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8'] 

uri = "mongodb+srv://viaathreatintel:rrDsKYeblTyDitLK@cluster0.mckr9yr.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
myclient = pymongo.MongoClient(uri)
mydb = myclient["iitk"]
mycol = mydb["threatintell"]


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
        return "Non-malicious hash"
    else:
        return "Malicious hash"


def dbSearch(target):
    if mycol.find_one({"ip":target}) is None:
        return "Non-malicious IP"
    else:
        return "Malicious IP"

# dbAtlas()

def fileScanResult(hashValue,result):
   
    fileHashCol = mydb["fileScanResult"]
   
    if fileHashCol.find_one({"hash":hashValue}):
        resultDict = fileHashCol.find_one({"hash":hashValue})["result"]
        resultDict[list(result.keys())[0]] = list(result.values())[0]
        print(resultDict)

        fileHashCol.update_one({"hash":hashValue},{"$set":{"result":resultDict}})
    else:
        fileHashCol.insert_one({"hash":hashValue,"result":result})

