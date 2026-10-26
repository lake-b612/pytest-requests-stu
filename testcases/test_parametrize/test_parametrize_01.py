import pytest


# #单参数，单次循环
# @pytest.mark.parametrize("key",["value"])
# def test_parametrize(key):
#     print("我是" + key)

#单参数，多次循环
#运行时，将数组里的值分别赋值给变量，每次复制时执行一次
@pytest.mark.parametrize("name",["安琪拉","黄忠","大乔"])
def test_parametrize(name):
    assert name == "安琪拉"

