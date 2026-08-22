import requests

url = "https://jsonplaceholder.typicode.com/users/1"

payload = {
    "email": "ramonsaturno@gmail",
}

response = requests.patch(url, json=payload)
print(response.status_code)

print(response.json())