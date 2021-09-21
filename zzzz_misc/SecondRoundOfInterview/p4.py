import requests
from bs4 import BeautifulSoup

url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=tablet&_sacat=0"

response = requests.get(url)
soup = BeautifulSoup(response.content, "lxml")

ul = soup.find("ul", {"class": "srp-results"})
li = ul.find("li", {"class": "s-item"})
price_span = li.find("span", {"class": "s-item__price"})

print(price_span.text)
