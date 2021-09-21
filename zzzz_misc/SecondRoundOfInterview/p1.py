import requests
from bs4 import BeautifulSoup

response = requests.get(
    "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=phone&_sacat=0")

soup = BeautifulSoup(response.content, "lxml")
element = soup.find(
    "ul", {"class": "srp-results srp-list clearfix"}).find(
        "div", {"class": "s-item__wrapper clearfix"}).find(
            "span", {"class": "s-item__price"}
        ).text
print(element)
