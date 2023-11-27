import requests

endpoint = "http://localhost:8000/api/"

#response = requests.get(endpoint, params={"abc": 123}, json={"query": "Hello, world!"})
#response = requests.post(endpoint, params={"abc": 123}, json={"title": "Hello, world!"})
#response = requests.post(endpoint, params={"abc": 123}, json={"content": "Hello, world!"}) #will give error
response = requests.post(endpoint, params={"abc": 123}, json={"title": None, "content": "Hello, world!"}) #will give error

print(response.json())
#print(response.headers)
#print(response.text)
#print(response.json()["message"])

#http response by defalut content type is text/html