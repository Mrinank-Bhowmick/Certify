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

    readme = open('README.md', 'w')
    readme.write("# My Followers\n\n")

    readme.write("<table>\n<tr>\n")
    for i, follower in enumerate(followers[:20]):
        if i > 0 and i % 10 == 0:
            readme.write("</tr>\n<tr>\n")
        readme.write(f'<td align="center"><a href="https://github.com/{follower["login"]}"><img src="{follower["avatar_url"]}&s=50" width="50" height="50" alt="{follower["login"]}" /><br />@{follower["login"]}</a></td>\n')
    readme.write("</tr>\n</table>")

    readme.write("\n<details><summary>🔽 Show more</summary>\n\n")

    readme.write("<table>\n<tr>\n")
    for i, follower in enumerate(followers[20:]):
        if i > 0 and i % 10 == 0:
            readme.write("</tr>\n<tr>\n")
        readme.write(f'<td align="center"><a href="https://github.com/{follower["login"]}"><img src="{follower["avatar_url"]}&s=50" width="70" height="70" alt="{follower["login"]}" /><br />@{follower["login"]}</a></td>\n')
    readme.write("</tr>\n</table>")

    readme.write("\n</details>")
    
    readme.close()

get_followers_avatar()
