import requests
params = {
      "email": "eve.holt@reqres.in",
      "password": "pistol"
    }
r = requests.post(url="https://reqres.in/api/register",params=params)
print(r.status_code)
print(r.json())


