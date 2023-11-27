import requests

endpoint = "http://localhost:8000/api/products/"
data = {"title": "This is a New Product"}

response = requests.post(endpoint, json=data) #will give error

print(response.json())