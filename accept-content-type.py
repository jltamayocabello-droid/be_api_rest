import requests

url = "https://jsonplaceholder.typicode.com/users"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}
payload = {
    "name": "Ana Marquez",
    "email": "ana@gmail"
}

response = requests.post(url, json=payload, headers=headers)

print(response.status_code)
print(response.json())