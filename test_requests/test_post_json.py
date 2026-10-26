import requests
json_data = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
  }
r = requests.post(url="https://reqres.in/api/register",json=json_data)
print(r.json())
print(r.status_code)