# issuicide

**issuicide** is a lightweight Python tool to bulk-create GitHub issues via the GitHub API.
Ideal for automated issue generation, testing, or (un)leashing controlled issue floods on repositories.

---

## Features

* Bulk-create hundreds or thousands of issues with customizable titles and bodies
* Supports multi-line issue bodies with markdown and emojis
* Automatically handles simple rate-limit cooldowns with configurable delays
* Easy to configure and run with minimal dependencies (`requests`)

---

## Requirements

* Python 3.6+
* `requests` library (`pip install requests`)
* GitHub Personal Access Token (classic) with **repo** permission

---

## Usage

1. Clone the repo or download `issuicide.py`
2. Edit the configuration variables at the top of the script:

   * `GITHUB_TOKEN`: Your GitHub Personal Access Token
   * `REPO_OWNER`: The target repository owner (user/org)
   * `REPO_NAME`: The target repository name
   * `START_ISSUE_NUMBER`: Number to start issue numbering from
   * `NUM_ISSUES`: Total number of issues to create
3. Customize `TITLE_TEMPLATE` and `BODY_TEMPLATE` as desired
4. Run the script:

   ```bash
   python issuicide.py
   ```

---

## Rate Limit Handling

**issuicide** detects HTTP 403 rate-limit errors and automatically switches to a cooldown mode, increasing the delay between issue creations to avoid API abuse detection. After cooldown, it resumes normal speed.

---

## Disclaimer

Use responsibly. Flooding repositories with issues may violate GitHub’s Terms of Service and can lead to account suspension. This tool is provided for educational or testing purposes only.
(actually just use it on an alt xd no one cares about this type of stuff (probably))

---

## License

MIT License

---
