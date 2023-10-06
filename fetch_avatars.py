import os
import requests

def get_followers_avatar():
    repo = os.getenv("GITHUB_REPOSITORY")
    user = repo.split('/')[0]
    followers_url = f"https://api.github.com/users/{user}/followers"
    headers = {'Authorization': f'token {os.getenv("GH_TOKEN")}'}
    response = requests.get(followers_url, headers=headers)
    followers = response.json()

    readme = open('README.md', 'w')
    readme.write("# My Followers\n\n")

    for follower in followers:
        readme.write(f"![{follower['login']}]({follower['avatar_url']}&s=100)\n")

    readme.close()

get_followers_avatar()
