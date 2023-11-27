import requests

product_id = input("What is the product id you want to delete?\n")
try:
    product_id = int(product_id)
except:
    print(f"{product_id} is Not valid.")
    product_id = None


endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"
response = requests.delete(endpoint) 

print(response.status_code, response.status_code == 204)