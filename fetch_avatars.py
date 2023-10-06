import os
import requests

def get_followers_avatar():
    repo = os.getenv("GITHUB_REPOSITORY")
    user = repo.split('/')[0]
    followers = []
    page = 1
    while True:
        followers_url = f"https://api.github.com/users/{user}/followers?page={page}"
        headers = {'Authorization': f'token {os.getenv("GH_PAT")}'}
        response = requests.get(followers_url, headers=headers)
        page_followers = response.json()
        if not page_followers:
            break
        followers.extend(page_followers)
        page += 1

    with open('README.md', 'r') as file:
        readme_content = file.readlines()

    followers_info = "\n<table>\n<tr>\n"
    for i, follower in enumerate(followers[:20]):
        if i > 0 and i % 10 == 0:
            followers_info += "</tr>\n<tr>\n"
        followers_info += f'<td align="center"><a href="https://github.com/{follower["login"]}"><img src="{follower["avatar_url"]}&s=50" width="50" height="50" alt="{follower["login"]}" /><br />@{follower["login"]}</a></td>\n'
    followers_info += "</tr>\n</table>"

    followers_info += "\n<details><summary>Show more</summary>\n\n"

    followers_info += "<table>\n<tr>\n"
    for i, follower in enumerate(followers[20:]):
        if i > 0 and i % 10 == 0:
            followers_info += "</tr>\n<tr>\n"
        followers_info += f'<td align="center"><a href="https://github.com/{follower["login"]}"><img src="{follower["avatar_url"]}&s=50" width="70" height="70" alt="{follower["login"]}" /><br />@{follower["login"]}</a></td>\n'
    followers_info += "</tr>\n</table>"

    followers_info += "\n</details>"

    for i, line in enumerate(readme_content):
        if '<!--Show_followers_here-->' in line:
            readme_content.insert(i+1, followers_info)
            break

    with open('README.md', 'w') as file:
        file.writelines(readme_content)

get_followers_avatar()
