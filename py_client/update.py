import requests

endpoint = "http://localhost:8000/api/products/1/update/"
data = {"title": "Hello from new world", "price": 129.99}
response = requests.put(endpoint, json=data) #will give error

print(response.json())