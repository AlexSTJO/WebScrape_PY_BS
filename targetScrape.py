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
        "url" : scrapeUrl(item)
    }
    return productDict

def scrapeName(item):
    name = item.find("div", class_="Truncate-sc-10p6c43-0 flAIvs")
    if  name == None:
        return None
    else:
        return name.text

def scrapeRating(item):
    rating = item.find("span", class_="RatingStars__StyledRatingStars-sc-k7ad82-0 kmUdOs")
    if rating == None:
        return rating
    else:
        return rating.text

def scrapePricing(item):
    pricing = item.find("span", class_="h-text-red")
    if pricing == None or "-" in pricing.text:
        return pricing
    else:
        return pricing.text

def scrapeUrl(item):
    parent = item.find("div", class_="styles__ProductCardItemInfoDiv-sc-h3r0um-0 idUsSc")
    if parent == None:
        return parent
    link_list = str(parent.find("a", href = True))
    if "href=" in link_list:
        urlend = link_list[link_list.find("href=") + 6:link_list.find('">')]
        return "target.com" + urlend
    else:
        return None


def targetScrapeMain(searchQ):
    URL = 'https://www.target.com/s?searchTerm=' + searchQ
    print(URL)
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, "html.parser")
    item_elements = soup.find_all('div', class_="styles__StyledCol-sc-fw90uk-0 fPNzT")

    for item in item_elements:
        productinfo = scrapeProductInfo(item)
        if None not in productinfo.values():
            f = open("productinfo.txt", "a")
            f.write(str(productinfo) + "\n")
            f.close

x = "boots"
targetScrapeMain(x)
