import requests

"""
params = {"firstName": "John", "lastName": "Smith"}  # query string
r = requests.get("https://httpbin.org/get", params=params)

r = requests.post("https://httpbin.org/post", data=params)

files = {"file": open("C://SMITA PERSONAL REPOSITORY//GITHUB CODE//PYTHON//PYTHON_REQUESTS//sample.csv", "rb"),
         "file1": open("C://SMITA PERSONAL REPOSITORY//GITHUB CODE//PYTHON//PYTHON_REQUESTS//sample.csv", "rb")}
r = requests.post("https://httpbin.org/post", files=files)

r = requests.get("https://api.github.com/events")

data = {"firstName": "John"}
r = requests.post("https://httpbin.org/post", json=data)

# headers
# Content-Type
# application/json
# text/plain
# text/javascript
# multipart/form-data

headers = {"content-type": "multipart-form-data"}
r = requests.post("https://httpbin.org/post", headers=headers)

# server sends cookie to client
# saved on browser
# session
# personalize
# track

url = "https://httpbin.org/cookies"
cookies = {"location": "India"}
r = requests.get(url, cookies=cookies)

r = requests.get("https://google.com")

requestsjar = requests.cookies.RequestsCookieJar()
requestsjar.set("userId", "John99", domain="httpbin.org", path="/cookies")
requestsjar.set("cartItem", "laptop", domain="httpbin.org", path="/cart")

r = requests.get(url, cookies=requestsjar)

print(r.url)
print("\n"*5)
print(r.request.headers)
print("\n"*5)
print(r.content)
print("\n"*5)
print(r.text)
print("\n"*5)
print(r.status_code)
print("\n"*5)
# print(r.json())
# print("\n"*5)
print(r.headers)
print("\n"*5)
print(r.cookies)
print("\n"*5)

r = requests.get("https://httpbin.org/status/404")
# r.raise_for_status()

# r = requests.get("https://httpbin.org/status/404", timeout=0.1)

# head verb gives headers from response for get, not body

r = requests.get("http://github.com", allow_redirects=True)
print(r.history)
print(r.url)
print(r.status_code)

# session
# persist state
# session id from server to client
# use this id from client

s = requests.Session()

username = {"userName": "John"}
location = {"location": "NewYork"}

set_cookie_url = "https://httpbin.org/cookies/set"
get_cookies_url = "https://httpbin.org/cookies"

s.get(set_cookie_url, params=username)
s.get(set_cookie_url, params=location)

r = s.get(get_cookies_url)
print(r.text)


def response_info(r, *args, **kwargs):
    print(r.url)
    print(r.status_code)
    print(r.text)
def response_headers(r, *args, **kwargs):
    print(r.headers)
hooks = {"response": (response_info, response_headers)}
r = requests.get("https://httpbin.org/get", hooks=hooks)

# hide ip with proxy
# control access
# firewall
# filter
# cache

proxies = {"https": "https://198.211.101.99:3128"}

r = requests.get("https://httpbin.org/ip", proxies=proxies)
print(r.text)

r = requests.get("https://github.com", verify="/path/to/CA")  # trusted CA  # or set to False
s = requests.session()
s.verify("path/to/CA")
"""

# multipart-form?
# allow origin?
