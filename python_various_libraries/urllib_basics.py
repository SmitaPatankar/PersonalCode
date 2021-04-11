from urllib.parse import urljoin

print(urljoin("https://www.google.com", "search"))
print(urljoin("https://www.google.com/", "search"))
print(urljoin("https://www.google.com", "/search"))
print(urljoin("https://www.google.com/", "/search"))

# https://www.google.com/search
