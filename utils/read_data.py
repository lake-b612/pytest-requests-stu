import yaml

file_path = r"D:\pycharm\ruance\pytest-requests\pytest-requests-stu\config\data.yaml"
with open(file_path, encoding="utf-8") as f:
    data = yaml.safe_load(f)
print(data)

print(data['hero'])
print(data['heros_name'])
print(data['heros'])
print(data['heros_name_list'])
print(data['history_today_params'])

def get_history_params():
    return data['history_today_params']