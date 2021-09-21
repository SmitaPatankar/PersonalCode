from bs4 import BeautifulSoup
from requests import session

s = session()

url = "https://www.carwale.com/api/v2/login/"
data = {
    "email": "smita.v.patankar@gmail.com", 
    "password": "*****", 
    "rememberMe": False
    }
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    }

print(s.headers)

response = s.post(url=url, data=data, headers=headers)

print(response.status_code)
print(response.content)
