from requests_html import HTMLSession
from bs4 import BeautifulSoup

s = HTMLSession()


def get_data(url):
    r = s.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup


def get_next_page(soup):
    page = soup.find("ul", {"class": "a-pagination"})
    if not page.find("li", {"class": "a-disabled a-last"}):
        url = "https://www.amazon.co.uk" + soup.find("li", {"class": "a-last"}).find("a")["href"]
        return url
    return ""


url = "https://www.amazon.co.uk/s?k=dslr+camera&ref=sr_gnr_aps"
while True:
    print(url)
    soup = get_data(url)
    url = get_next_page(soup)
    if not url:
        print("no more urls")
        break
