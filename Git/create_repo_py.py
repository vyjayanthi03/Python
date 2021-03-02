from github import Github

token = Github("658ee0869a6e13df62ac0ec49ac1986b952e8477")
user_data = token.get_user("Abdurrahman512")
create_repo = user_data.create_repo("aaa")

