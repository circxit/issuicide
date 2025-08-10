import requests
import time

GITHUB_TOKEN = "TOKEN"
REPO_OWNER = "repo-owner"
REPO_NAME = "repo-name"
START_ISSUE_NUMBER = 1
NUM_ISSUES = 100

TITLE_TEMPLATE = "Issue #{n}"
BODY_TEMPLATE = """\
Use this
for multiple
lines of the issue :D
"""

api_url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues"
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

normal_delay = 2
cooldown_delay = 10
cooldown_issues_remaining = 0

for i in range(START_ISSUE_NUMBER, START_ISSUE_NUMBER + NUM_ISSUES):
    title = TITLE_TEMPLATE.format(n=i)
    payload = {"title": title, "body": BODY_TEMPLATE}
    response = requests.post(api_url, json=payload, headers=headers)

    if response.status_code == 201:
        print(f"Created issue #{i}")
    else:
        print(f"Failed to create issue #{i}: {response.status_code} - {response.text}")
        if response.status_code == 403:
            print("⚠️ Rate limit hit! Entering cooldown: 5 seconds delay for next 10 issues.")
            cooldown_issues_remaining = 30

    if cooldown_issues_remaining > 0:
        time.sleep(cooldown_delay)
        cooldown_issues_remaining -= 1
    else:
        time.sleep(normal_delay)
