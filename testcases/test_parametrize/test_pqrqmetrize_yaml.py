import allure
import pytest
import requests
from utils.read_data import get_history_params

@pytest.mark.parametrize("month,day",get_history_params())
@allure.feature("历史上的今天模块")
@allure.story("查询程序员历史事件")
@allure.title("传入{month}-{day}查询历史事件")  # 参数化可以直接拿变量
@allure.severity(allure.severity_level.NORMAL)
def test_get_history_today(month, day):
  url = "https://uapis.cn/api/v1/history/programmer?month=9&day=12"
  params = {
      "month": month,
      "day": day,
  }
  r = requests.get(url, params=params)
  assert r.status_code == 200
  result = r.json()
  assert result["message"] == "获取成功"
  assert result["date"] == "09-12"
  assert result["events"][0]["year"] == 1958
