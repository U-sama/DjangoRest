import requests

endpoint = "http://localhost:8000/api/"

response = requests.get(endpoint, params={"abc": 123}, json={"query": "Hello, world!"})

print(response.json())
#print(response.headers)
#print(response.text)
#print(response.json()["message"])

#http response by defalut content type is text/html