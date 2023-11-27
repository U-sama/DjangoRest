import requests

endpoint = "http://localhost:8000/api/products/"
data = {"title": "This is a New Product"}

response = requests.get(endpoint) #will get all the product

print(response.json())