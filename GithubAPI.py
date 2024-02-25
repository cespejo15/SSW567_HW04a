import requests
import json

username = input("Input Username: ") 
response = requests.get(f"https://api.github.com/users/{username}/repos")
userRepos = response.json()

if userRepos != []:
    for repo in userRepos:
        response = requests.get(f"https://api.github.com/repos/{username}/{repo['name']}/commits")
        data = response.json()
        count = len(data)
        print(f"Repo: {repo['name']} Number of commits: {str(count)}")
else:
    print("Failed to retrieve repositories.")
