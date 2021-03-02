from github import Github

user = "Abdurrahman512"
password ="3@MyGithub3"
token="dbdc64d892bc933f4e25011efeef9cb71a666899"
g1 = Github(token)
g2 = Github(user, password)

user = g2.get_user()

#Get repositories for authenticated user
repositories = user.get_repos()


#Get assignees for a repo
repo = org.get_repo('community')
assignees = repo.get_assignees()
assignees_list = []
for assignee in assignees:
    assignees_list.append(assignee)
print (assignees)

#Check if an assignee is in list of assignees
has_in_assignees = repo.has_in_assignees(assignees_list[0])
print (has_in_assignees)

#Get labels used in a repo
labels = repo.get_labels()
label_list_name = []
for label in labels:
	label_list_name.append(label.name)

#Get label used in a repo by its name
label = repo.get_label(label_list_name[0])
print (label)