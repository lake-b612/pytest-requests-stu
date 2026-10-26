import pytest

# #数组
# @pytest.mark.parametrize("name,word",[["安琪拉","火焰.."],["黄忠","周日被..."],["鲁班","啦啦啦"]])
# def testparametrize_02(name,word):
#     print(f'{name}的台词是{word}')

# #元组
# @pytest.mark.parametrize("name,word", [("安琪拉", "火焰.."),("黄忠", "周日被..."),("鲁班", "啦啦啦")])
# def testparametrize_02(name, word):
#     print(f'{name}的台词是{word}')

@pytest.mark.parametrize("name,word", [["安琪拉", "火焰.."]])
def testparametrize_02(name, word):
    print(f'{name}的台词是{word}')

