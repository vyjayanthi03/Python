from github import Github

# First create a Github instance:

# using username and password
g = Github("Abdurrahman512", "3@MyGithub3")

# or using an access token
g = Github("4d863187153c32baef06df34861ce9064b3b9be7")

# Github Enterprise with custom hostname
g = Github(base_url="https://gtihub.com/api/v3", login_or_token="4d863187153c32baef06df34861ce9064b3b9be7")

user =  g.get_repo("PyGithub/PyGithub")
#print(user)