import pytest
import requests

def setup_function():
    print("准备测试数据")

def teardown_function():
    print("请理测试数据")


def test_register():
  json_data = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
  }
  r = requests.post(url="https://reqres.in/api/register",json=json_data)
  assert r.status_code == 200
  result = r.json()
  assert result['id'] == 4
  assert result['token'] == "QpwL5tke4Pnpja7X4"
  assert result['_meta']["powered_by"] == "ReqRes"
  assert result['_meta']["docs_url"] == "https://app.reqres.in/documentation"

def test_get():
  # 北京经纬度 纬度39.9042,经度116.4074
  url = "https://api.open-meteo.com/v1/forecast"
  params = {
      "latitude": 39.9042,
      "longitude": 116.4074,
      "current": "temperature_2m"
  }
  r = requests.get(url, params=params)
  assert r.status_code == 200
  result = r.json()
  assert "generationtime_ms" in result
  assert result["generationtime_ms"] > 0

  assert result["utc_offset_seconds"] == 0
  assert result["current_units"]["time"] == "iso8601"
  assert "temperature_2m" in result["current"]


if __name__ == "__main__":
    pytest.main()
