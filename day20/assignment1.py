import json

json_data = '{"name":"June","contact":{"email":"june@example.com","city":"Paris"}}'
data = json.loads(json_data)

print(data["contact"])
