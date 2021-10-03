import requests

BASE = 'http://3.231.167.221:5000/'

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
