import csv
import json
import pandas as pd

with open('C:/Users/SSS2015046/Desktop/test.json', 'r') as j: # Assigning file path to read
    jdata = json.load(j) # loading json file data to jdata
result = [] # to store output value
for data in jdata['results']: # to find no of elements and it will get element one by one
    output = {} # it will store the element value for specified key in dict format
    output['id'] = data['id'] # specified key values
    for k in data['properties'].keys(): # it will get sub elements of above element
        output[k] = data['properties'][k] # here we call key base values
    result.append(output) # all the collected data is stored in result by appending method
    print(result)
df = pd.DataFrame(result) # converting results into DataFrames(in to structured data with lables)
print(df)
df.to_csv('C:/Users/SSS2015046/Desktop/test1.csv', index= False) # Convering DataFrames to CSV file