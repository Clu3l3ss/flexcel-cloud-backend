import requests

BASE = 'http://127.0.0.1:5000/'

response = requests.put(BASE + 'storage/3', {'type' : 'flow', 'value' : {'TEST' : 'TEST'}})
print(response.json())
print(response.status_code)
input()
response = requests.get(BASE + 'storage/3', {'type' : 'flow'})
print(response.json())
print(response.status_code)
input()
#response = requests.delete(BASE + 'storage/3', {'type' : 'flow'})
#print(response.json())
#print(response.status_code)
#input()