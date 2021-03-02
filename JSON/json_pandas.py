import csv
import json
import pandas as pd

with open('C:/Users/SSS2015046/Desktop/test.json', 'r') as j:
    jdata = json.load(j)
# jdata = pd.read_json('F:/Python/test.json')
    # print(jdata)

result = [ ]
for jdata1 in jdata['results']:
    output = { }
    output['id'] = jdata1['id']
    for key,values in jdata1['properties'].items():
        # print(key,values)
        output[key] = str(jdata1['properties'][key])

    result.append(output)
    # print(result)
    df = pd.DataFrame(result)
    print(df)
    df.to_csv('C:/Users/SSS2015046/Desktop/jsontocsv.csv', index=False)
    # data = pd.read_csv('/F:/Python/jsontocsv.csv')