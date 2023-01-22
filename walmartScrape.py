from unicodedata import name
import requests
from bs4 import BeautifulSoup

HEADERS = ({'User-agent' :
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/107.0.0.0 Safari/537.36',
                    'Accept-Language': 'en-US, en;q=0.5'})

def scrapeProductInfo(item):
    productDict = {
        "name" : scrapeName(item),
        "rating" : scrapeRating(item),
        "pricing" : scrapePricing(item),
        "deliveryDate" : scrapeDeliveryDate(item),
        "url" : scrapeUrl(item)
    }
    return productDict

def scrapeName(item):
    name = item.find("span", class_="w_iUH7")
    if name == None:
        return name
    else:
        return name.text

def scrapeRating(item):
    rating = item.find("div", class_="flex items-center mt2")
    if rating == None:
        return rating
    else:
        return rating.text

def scrapePricing(item):
    pricing = item.find("div", class_="mr1 mr2-xl b black lh-copy f5 f4-l")
    if pricing == None:
        return pricing
    else:
        return pricing.text

def scrapeDeliveryDate(item):
    date = item.find("div", class_='mt2 mb2')
    if date == None:
        return date
    else:
        return date.text

def scrapeUrl(item):
    parent = item.find("div", class_="absolute w-100 h-100 z-1 hide-sibling-opacity")
    if parent == None:
        return None
    link_list = str(parent.find("a", href = True))
    if "href=" in link_list:
        urlend =  link_list.find[("href=") + 6:link_list.find('">')]
        return "walmart.com" + urlend
    else:
        return None


def walmartScrapeMain(SearchQ):
    URL = "https://www.walmart.com/search?q=" + SearchQ
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, "html.parser")
    item_elements = soup.find_all("div", class_="mb1 ph1 pa0-xl bb b--near-white w-25")
    for item in item_elements:
        productinfo = scrapeProductInfo(item)
    if None not in productinfo.values():
        f = open("productinfo.txt", "a")
        f.write(str(productinfo) + "\n")
        f.close
