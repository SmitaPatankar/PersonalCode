import requests
from bs4 import BeautifulSoup

page = requests.get("http://marketwatch.com")
soup = BeautifulSoup(page.content, "html.parser")

for i in soup.select("p"):  # tags
    print(i)
print("\n"*5)

for i in soup.select("p a"):  # tags within tags
    print(i)
print("\n"*5)

for i in soup.select("p,a"):  # multiple tags
    print(i)
print("\n"*5)

for i in soup.select(".element__options"):  # class
    print(i)
print("\n"*5)

for i in soup.select(".latestNews.j-scrollElement"):  # multiple classes with spaces
    print(i)
print("\n"*5)

for i in soup.select("ul.latestNews.j-scrollElement"):  # tag and classes with spaces
    print(i)
print("\n"*5)

page = requests.get("http://docs.python-requests.org/en/master/user/advanced/#advanced")
soup = BeautifulSoup(page.content, "html.parser")

for i in soup.select("div#advanced-usage"):  # tag and id
    print(i)
print("\n"*5)
