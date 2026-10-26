import requests
# 北京经纬度 纬度39.9042,经度116.4074
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude":39.9042,
    "longitude":116.4074,
    "current":"temperature_2m"
}
r = requests.get(url,params=params)
print(r.status_code)
print(r.json())
