import requests

# Get data from github api and store it in response variable. Search for `github api docs` and find link to api from there. We selected `Pull Requests` to get link for pull request api
response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

# json() function converts data from api to dictionary under the hood. So the type of `complete_detail` is list of dictionaries
complete_detail = response.json()

# Print the name of each user who raised the pull request in this repository
for user in complete_detail:
    print(user["user"]["login"])