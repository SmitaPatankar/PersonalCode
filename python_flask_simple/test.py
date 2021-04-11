# import libraries

import requests
import json

# create user

# url = "http://127.0.0.1:5000/user"
# data = {"name": "Admin", "password": "12345"}
# headers = {"content-type": "application/json"}
# response = requests.post(url=url, data=json.dumps(data), headers=headers)

url = "http://127.0.0.1:5000/user"
data = {"name": "Anthony", "password": "12345"}
headers = {"content-type": "application/json"}
response = requests.post(url=url, data=json.dumps(data), headers=headers)

# login

# url = "http://127.0.0.1:5000/login"
# headers = {"content-type": "application/json"}
# auth = ("Admin", "12345")
# response = requests.get(url=url, headers=headers, auth=auth)

# url = "http://127.0.0.1:5000/login"
# headers = {"content-type": "application/json"}
# auth = ("Anthony", "12345")
# response = requests.get(url=url, headers=headers, auth=auth)

# url = "http://127.0.0.1:5000/login"
# headers = {"content-type": "application/json"}
# response = requests.get(url=url, headers=headers, auth=None)

# url = "http://127.0.0.1:5000/login"
# headers = {"content-type": "application/json"}
# auth = ("wronguser", "12345")
# response = requests.get(url=url, headers=headers, auth=auth)

# url = "http://127.0.0.1:5000/login"
# headers = {"content-type": "application/json"}
# auth = ("Admin", "wrongpassword")
# response = requests.get(url=url, headers=headers, auth=auth)

# get users

# url = "http://127.0.0.1:5000/user"
# headers = {"content-type": "application/json", "x-access-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiIxNTI2ZmZhYi0xYzE4LTRhYjItODFhNC02OTc4MzVlZTBhOWQiLCJleHAiOjE2MDk1ODc0NDl9.raae_06GbEqAqLSsmbz_Zk6jcFa-3EFTuDMgBUVB5D4"}
# response = requests.get(url=url, headers=headers)

# url = "http://127.0.0.1:5000/user"
# headers = {"content-type": "application/json", "x-access-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwdWJsaWNfaWQiOiIxNTI2ZmZhYi0xYzE4LTRhYjItODFhNC02OTc4MzVlZTBhOWQiLCJleHAiOjE2MDk1ODc0NDl9.raae_06GbEqAqLSsmbz_Zk6jcFa-3EFTuDMgBUVB5D4"}
# response = requests.get(url=url, headers=headers)

# get user

# url = "http://127.0.0.1:5000/user/1526ffab-1c18-4ab2-81a4-697835ee0a9d"
# headers = {"content-type": "application/json"}
# response = requests.get(url=url, headers=headers)

# url = "http://127.0.0.1:5000/user/wrong_public_id"
# headers = {"content-type": "application/json"}
# response = requests.get(url=url, headers=headers)

# promote user

# url = "http://127.0.0.1:5000/user/1526ffab-1c18-4ab2-81a4-697835ee0a9d"
# headers = {"content-type": "application/json"}
# response = requests.put(url=url, headers=headers)

# delete user

# url = "http://127.0.0.1:5000/user/dd90eb87-959d-4ea0-8365-8dc66906f77d"
# headers = {"content-type": "application/json"}
# response = requests.delete(url=url, headers=headers)

# print response

# print(response.status_code)
# try:
#     print(json.loads(response.content))
# except:
#     print(response.content)
#     print(response.headers)
