import requests,re,os,sys
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

# sys.path.insert(1,os.getcwd()+"/../DbHandler")
sys.path.insert(1,"F:\Inernship\IITK\\threat-intel\DbHandler")
from dbFile import dbHashStore

def process_page(page_number):
    #the function will generate all the links
    url = f"https://virusshare.com/hashfiles/VirusShare_{str(page_number).zfill(5)}.md5"
    print("Processing:", url)

    req = requests.get(url)
    content = BeautifulSoup(req.content, 'html.parser')
    print(f"Got content of {url}")

    hashValuesList = re.findall(r"[0-9a-z]{32}",str(content))

    dbHashStore(hashValuesList,page_number)

def main():
    #for the no. of pages
    # pageno = range(485)
    pageno = range(100)
    
    #parallel links will be loaded and it is set to 10
    with ThreadPoolExecutor() as executor:
        
        futures = [executor.submit(process_page, i) for i in pageno]
        print("Printing Futures:\n\n",futures)
        #the parallel executions will be completed
        results = [future.result() for future in futures]
        # with open("result.txt",'w') as fp:
        #     fp.write(str(results))
        # print("Printing Results:\n\n",str(results)[:500])

    #the content from pages is being extracted here
    # for j, content in enumerate(results):
    #     print(f"Content of page {j + 1}:", content)

# if __name__ == "__main__":
#     main()