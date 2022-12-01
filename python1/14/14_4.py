import json

# 用loads()读取JSON(loads->load string)
# stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
# jsonDataAsPythonValue = json.loads(stringOfJsonData)
# print(jsonDataAsPythonValue)

# 用dumps函数写出JSON(dumps->dump string)
pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
stringOfJsonData = json.dumps(pythonValue)
print(stringOfJsonData)