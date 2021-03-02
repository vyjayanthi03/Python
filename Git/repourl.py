import requests
from pprint import pprint

# github username
username = "Abdurrahman512"

# url to request

# url = "https://api.github.com/users/Abdurrahman512"
# repos_url = "https://api.github.com/users/Abdurrahman512/repos"
repo_url = "https://api.github.com/repos/Abdurrahman512/Practice"


# make the request and return the json

# User Data
# user_data = requests.get(url).json()

# All repos data
# repos_data = requests.get(repos_url).json()

# Particular repos data
repo_data = requests.get(repo_url).json()

# pretty print JSON data

# pprint(user_data)
# pprint(repos_data)
pprint(repo_data)



import json
from flatten_json import flatten
with open('C:/Users/SSS2020215/Desktop/test.json', 'r') as j:
    data = json.load(j)
for col in data['results']:
    for col in col.items():
        print(col)
        
        
        
        
        
        
        
        
        select * from devops.survey_import where list_all_applications like '%Edivate%'

insert int into devops.survey_backup

select max(length(handling_database_schema_changes)) from devops.survey_import