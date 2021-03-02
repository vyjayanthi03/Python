from github import Github

token = Github("658ee0869a6e13df62ac0ec49ac1986b952e8477")
user_data = token.get_user("Abdurrahman512")
user_repo = user_data.get_repo("Practice")

for repo in user_data.get_repos():
    print("repo_name :", repo.name)
    print("repo_id: " ,repo.id)
    print("repo_created_date:" , repo.created_at)
    print("totalcommits: ", repo.get_commits().totalCount)
    print("lastcommit_date: ", repo.updated_at)
