import json
with open('existing_json.json', 'r') as file:
    existing_data = json.load(file)
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
existing_data.append(x)
with open('existing_json.json', 'w') as file:
    json.dump(existing_data, file, indent=4)