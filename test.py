import json

with open('data.json', 'r') as json_file:
    data_dict = json.load(json_file)

    print(data_dict)
    print(type(data_dict))