import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["iitk"]
mycol = mydb["threatintell"]

def dbStore(resultList):
    # print(result)
    for i in resultList:
        if mycol.find_one({"ip":i[0]}) is None:
            mycol.insert_one({"ip":i[0],"location":i[1]})


def dbSearch(target):
    if mycol.find_one({"ip":target}) is None:
        return "Non-malicious IP"
    else:
        return "Malicious IP"