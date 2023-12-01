import pymongo
import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8'] 

uri = "mongodb+srv://viaathreatintel:rrDsKYeblTyDitLK@cluster0.mckr9yr.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
myclient = pymongo.MongoClient(uri)
mydb = myclient["iitk"]
mycol = mydb["threatintell"]

def dbUrlStore(url):
    # print(result)
    urlValue = url.strip()
    if mycol.find_one({"url":urlValue}) is None:
        mycol.insert_one({"url":urlValue})

        print(f"Inserted: {urlValue}")

with open("urls.txt","r") as fp:
    for link in fp.readlines():
        dbUrlStore(link)

