import json
with open('C:/Users/SSS2015046/Desktop/test.json', 'r') as test:
    data = json.load(test)

for data1 in data['results']:
    print(data1)
    # print(data1['properties']['email'])


