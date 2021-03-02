from github import Github
import repo
import urllib
import requests
import pprint
url ="https://api.github.com/users/Abdurrahman512/Practice"
repo = requests.get(url).json()
print(type(repo))
pprint(repo)
# print("Repo name: ",repo.name)
# print("Repo id: ",repo.id)
# print("Repo created on: ",repo.created_at)
# print("Repo last modified date: ",repo.last_modified)
# print("Total commits count: ",repo.get_commits().totalCount)
# for language in repo.get_language():
#     print(language)
#
#     if data == None or data == '':
#         print('I got a null or empty string value for data in a file')
#     else:
#         js = json.loads(str(data))
