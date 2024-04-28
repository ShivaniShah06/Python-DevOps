# Program to demonstrate integration with GitHub to fetch the 
# details of Users who created Pull requests(Active) on Kubernetes Github repo.
import requests

link = input("\nEnter the link for the open source Github API beginning with 'https://' to get the names of users who raised the PR for the repo along with PR count:")
# One example for the link is  https://api.github.com/repos/docker/compose/pulls

# Make a GET request to fetch pull requests data from the GitHub API
response = requests.get(link)

# If the request is successful
if response.status_code == 200:
    # Convert the JSON response to a dictionary
    pull_requests = response.json()
    # Create an empty dictionary to store PR creators and their counts
    pr_creators = {}

    # Iterate through each pull request and extract the creator's name
    for pull_request in pull_requests:
        creator = pull_request["user"]["login"]
        if creator in pr_creators:
            pr_creators[creator] += 1
        else:
            pr_creators[creator] = 1

    # Display the dictionary of PR creators and their counts
    print("PR Creators & Counts:")
    for creator, count in pr_creators.items():
        print(f"{creator}: {count}PRs")
# If the request fails
else:
    print(f"Failed to fetch data from {link}: response_code={response.status_code}")