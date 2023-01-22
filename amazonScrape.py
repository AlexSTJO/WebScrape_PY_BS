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
    name = item.find("span", class_="a-size-base-plus a-color-base a-text-normal")
    if  name == None:
        return name
    else:
        return name.text

def scrapeRating(item):
    rating = item.find("span", class_="a-icon-alt")
    if rating == None:
        return rating
    else:
        return rating.text

def scrapePricing(item):
    pricing = item.find("span", class_="a-price-whole")
    if pricing == None:
        return pricing
    else:
        return pricing.text

def scrapeDeliveryDate(item):
    date = item.find("div", class_="a-row a-size-base a-color-secondary s-align-children-center")
    if date == None:
        return date
    else:
        return date.text

def scrapeUrl(item):
    parent = item.find("div", class_="s-product-image-container")
    if parent == None:
        return parent
    link_list = str(parent.find("a", href = True))
    if "href=" in link_list and "/gp/" not in link_list:
        urlend = link_list[link_list.find("href=") + 6:link_list.find('">')]
        return "amazon.com" + urlend
    else:
        return None

#ask user for amazon item and create page through requests
def scrapeMain(searchQ):
    URL ='https://www.amazon.com/s?k=' + searchQ
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, "html.parser")
    item_elements = soup.find_all("div", class_="a-section a-spacing-base")
    if item_elements == []:
        item_elements = soup.find_all("div", class_="a-section a-spacing-base a-text-center")

    for item in item_elements:
        productinfo = scrapeProductInfo(item)
        if None not in productinfo.values():
            f = open("productinfo.txt", "a")
            f.write(str(productinfo) + "\n")
            f.close



