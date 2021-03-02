from github import Github
from git import *
token = Github("71ff18e2e2034b2e9207b3c22a8cc91c1d5de944")
user_data = token.get_user("Abdurrahman512")
user_repo = user_data.get_repo("Practice")

for repo in user_data.get_repos():
    print("repo_name :", repo.name)
    print("repo_id:", repo.id)
    print("repo_created_date:", repo.created_at)
    print("totalcommits:", repo.get_commits().totalCount)
    print("lastcommit_date:", repo.updated_at)