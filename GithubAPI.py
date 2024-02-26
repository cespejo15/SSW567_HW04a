import requests
import json

def Repositories(username):
    responseRepo = requests.get(f"https://api.github.com/users/{username}/repos")

    if responseRepo.status_code == 200:
        userRepos = json.loads(responseRepo.text)
        if userRepos != []:
            repoList = []
            for repo in userRepos:
                responseCommits = requests.get(f"https://api.github.com/repos/{username}/{repo['name']}/commits")
                if responseCommits.status_code == 200:
                    userCommits = json.loads(responseCommits.text)
                    count = len(userCommits)
                    repoList.append(f"Repo: {repo['name']} Number of commits: {count}")
                else:
                    repoList.append(f"Commit retrieval faliure for {repo['name']}")
            print(repoList)
            return repoList
        else:
            return "User has no repositories."
    else:
        return "Repository retrieval faliure or Repository not found"


username = input("Input Github Username: ") 
Repositories(username)
