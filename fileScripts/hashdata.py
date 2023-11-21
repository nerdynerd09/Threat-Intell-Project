import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

def process_page(page_number):
    #the function will generate all the links
    url = f"https://virusshare.com/hashfiles/VirusShare_{str(page_number).zfill(5)}.md5"
    print("Processing:", url)

    req = requests.get(url)
    content = BeautifulSoup(req.content, 'html.parser')

    return content

def main():
    #for the no. of pages
    pageno = range(485)
    
    #parallel links will be loaded and it is set to 10
    with ThreadPoolExecutor(max_workers=10) as executor:
        
        futures = [executor.submit(process_page, i) for i in pageno]

        #the parallel executions will be completed
        results = [future.result() for future in futures]

    #the content from pages is being extracted here
    for j, content in enumerate(results):
        print(f"Content of page {j + 1}:", content)

if __name__ == "__main__":
    main()