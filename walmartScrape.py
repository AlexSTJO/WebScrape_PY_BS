from unicodedata import name
import requests
from bs4 import BeautifulSoup

HEADERS = ({'User-agent' :
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/107.0.0.0 Safari/537.36',
                    'Accept-Language': 'en-US, en;q=0.5'})

def scrapeProductInfo(item):
    productDict = {
        'name' : scrapeName(item)
    }

def scrapeName(item):
    
def walmartScrapeMain(SearchQ):
    URL = "https://www.walmart.com/search?q=" + SearchQ
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, "html.parser")
    item_elements = soup.find_all("div", class_="mb1 ph1 pa0-xl bb b--near-white w-25")
    for item in item_elements:
        scrapeProductInfo(item)

searchQ = "boots"
walmartScrapeMain(searchQ)
