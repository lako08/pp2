import json

json_string = '{"name":"Ali","age":20}'
data = json.loads(json_string)

print(data["name"])
print(data["age"])