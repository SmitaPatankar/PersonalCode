# for local execution
# uncomment create_tables() from app.py
# add secret_key to app.py
# python app.py - one terminal
# python api_caller.py - another terminal

# for proper deployed execution
# follow deployment instructions from notes.md
# python api_caller.py

import requests
import json

print("register user - first user i.e. admin")
resp = requests.post(url='http://127.0.0.1:5000/register', data=json.dumps({"username": "bob", "password": "asdf"}), headers={"Content-Type": "application/json"})
print(resp.content)
print(resp.status_code)

print("register user - second user i.e. non-admin")
resp = requests.post(url='http://127.0.0.1:5000/register', data=json.dumps({"username": "jon", "password": "pqrs"}), headers={"Content-Type": "application/json"})
print(resp.content)
print(resp.status_code)

print("register user - repeated user")
resp = requests.post(url='http://127.0.0.1:5000/register', data=json.dumps({"username": "jon", "password": "pqrs"}), headers={"Content-Type": "application/json"})
print(resp.content)
print(resp.status_code)

print("login admin user i.e. get fresh token and initial refresh token")
resp = requests.post(url='http://127.0.0.1:5000/login', data=json.dumps({"username": "bob", "password": "asdf"}), headers={"Content-Type": "application/json"})
print(resp.content)
print(resp.status_code)
fresh_token = json.loads(resp.content)["access_token"]
initial_refresh_token = json.loads(resp.content)["refresh_token"]

print("login non admin user")
resp = requests.post(url='http://127.0.0.1:5000/login', data=json.dumps({"username": "bob", "password": "asdf"}), headers={"Content-Type": "application/json"})
print(resp.content)
print(resp.status_code)
non_admin_fresh_token = json.loads(resp.content)["access_token"]

print("login - incorrect user")
resp = requests.post(url='http://127.0.0.1:5000/login', data=json.dumps({"username": "blah", "password": "asdf"}), headers={"Content-Type": "application/json"})
print(resp.content)
print(resp.status_code)

print("login - incorrect password")
resp = requests.post(url='http://127.0.0.1:5000/login', data=json.dumps({"username": "bob", "password": "blah"}), headers={"Content-Type": "application/json"})
print(resp.content)
print(resp.status_code)

print("refresh token of user")
resp = requests.post(url='http://127.0.0.1:5000/refresh', headers={"Content-Type": "application/json", "Authorization": "Bearer {}".format(initial_refresh_token)})
print(resp.content)
print(resp.status_code)
refresh_token = json.loads(resp.content)["access_token"]

print("refresh token of user - missing initial refresh token")
resp = requests.post(url='http://127.0.0.1:5000/refresh', headers={"Content-Type": "application/json"})
print(resp.content)
print(resp.status_code)

print("get user")
resp = requests.get(url='http://127.0.0.1:5000/user/1', headers={"Authorization": "Bearer {}".format(fresh_token)})
print(resp.content)
print(resp.status_code)

print("get user - incorrect user")
resp = requests.get(url='http://127.0.0.1:5000/user/20', headers={"Authorization": "Bearer {}".format(fresh_token)})
print(resp.content)
print(resp.status_code)

print("get user - missing token")
resp = requests.get(url='http://127.0.0.1:5000/user/1')
print(resp.content)
print(resp.status_code)

print("create store")
resp = requests.post(url='http://127.0.0.1:5000/store/test1', data=json.dumps({"items": []}), headers={"Content-Type": "application/json", "Authorization": "Bearer {}".format(fresh_token)})
print(resp.content)
print(resp.status_code)

print("create store - repeat store")
resp = requests.post(url='http://127.0.0.1:5000/store/test1', data=json.dumps({"items": []}), headers={"Content-Type": "application/json", "Authorization": "Bearer {}".format(fresh_token)})
print(resp.content)
print(resp.status_code)

print("get store")
resp = requests.get(url='http://127.0.0.1:5000/store/test1', headers={"Authorization": "Bearer {}".format(fresh_token)})
print(resp.content)
print(resp.status_code)

print("get store - incorrect store")
resp = requests.get(url='http://127.0.0.1:5000/store/test20', headers={"Authorization": "Bearer {}".format(fresh_token)})
print(resp.content)
print(resp.status_code)

print("get stores")
resp = requests.get(url='http://127.0.0.1:5000/stores', headers={"Authorization": "Bearer {}".format(fresh_token)})
print(resp.content)
print(resp.status_code)

print("create item")
resp = requests.post(url='http://127.0.0.1:5000/item/myitem', data=json.dumps({"price": 1, "store_id": 1}), headers={"Content-Type": "application/json", "Authorization": "Bearer {}".format(fresh_token)})
print(resp.content)
print(resp.status_code)

print("create item - repeat item")
resp = requests.post(url='http://127.0.0.1:5000/item/myitem', data=json.dumps({"price": 1, "store_id": 1}), headers={"Content-Type": "application/json", "Authorization": "Bearer {}".format(fresh_token)})
print(resp.content)
print(resp.status_code)

print("get item")
resp = requests.get(url='http://127.0.0.1:5000/item/myitem', headers={"Authorization": "Bearer {}".format(fresh_token)})
print(resp.content)
print(resp.status_code)

print("get item - incorrect item")
resp = requests.get(url='http://127.0.0.1:5000/item/blahitem', headers={"Authorization": "Bearer {}".format(fresh_token)})
print(resp.content)
print(resp.status_code)

print("get items")
resp = requests.get(url='http://127.0.0.1:5000/items', headers={"Authorization": "Bearer {}".format(fresh_token)})
print(resp.content)
print(resp.status_code)

print("update item")
resp = requests.put(url='http://127.0.0.1:5000/item/myitem', data=json.dumps({"price": 12, "store_id": 1}), headers={"Content-Type": "application/json", "Authorization": "Bearer {}".format(fresh_token)})
print(resp.content)
print(resp.status_code)

print("update item - new item")
resp = requests.put(url='http://127.0.0.1:5000/item/mynewitem', data=json.dumps({"price": 12, "store_id": 1}), headers={"Content-Type": "application/json", "Authorization": "Bearer {}".format(fresh_token)})
print(resp.content)
print(resp.status_code)

print("update item - non admin user")
resp = requests.put(url='http://127.0.0.1:5000/item/mynewitem', data=json.dumps({"price": 12, "store_id": 1}), headers={"Content-Type": "application/json", "Authorization": "Bearer {}".format(non_admin_fresh_token)})
print(resp.content)
print(resp.status_code)

print("delete item")
resp = requests.delete(url='http://127.0.0.1:5000/item/myitem', headers={"Authorization": "Bearer {}".format(fresh_token)})
print(resp.content)
print(resp.status_code)

print("delete item - incorrect item")
resp = requests.delete(url='http://127.0.0.1:5000/item/blahitem', headers={"Authorization": "Bearer {}".format(fresh_token)})
print(resp.content)
print(resp.status_code)

print("delete store")
resp = requests.delete(url='http://127.0.0.1:5000/store/test1', headers={"Authorization": "Bearer {}".format(fresh_token)})
print(resp.content)
print(resp.status_code)

print("logout non-admin user")
resp = requests.post(url='http://127.0.0.1:5000/logout', headers={"Content-Type": "application/json", "Authorization": "Bearer {}".format(non_admin_fresh_token)})
print(resp.status_code)
print(resp.content)

print("get stores - logged out user i.e. token is not valid")
resp = requests.get(url='http://127.0.0.1:5000/stores', headers={"Authorization": "Bearer {}".format(fresh_token)})
print(resp.content)
print(resp.status_code)

print("delete non-admin user")
resp = requests.delete(url='http://127.0.0.1:5000/user/2', headers={"Authorization": "Bearer {}".format(fresh_token)})
print(resp.content)
print(resp.status_code)

print("delete user - incorrect user")
resp = requests.delete(url='http://127.0.0.1:5000/user/11', headers={"Authorization": "Bearer {}".format(fresh_token)})
print(resp.content)
print(resp.status_code)

print("delete admin user")
resp = requests.delete(url='http://127.0.0.1:5000/user/1', headers={"Authorization": "Bearer {}".format(fresh_token)})
print(resp.content)
print(resp.status_code)