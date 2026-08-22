import requests

url = "https://jsonplaceholder.typicode.com/users/1"

payload = {
    "name": "Ramon",
    "email": "ramon@gmail",
}

response = requests.put(url, json=payload)
print(response.status_code)

print(response.json())