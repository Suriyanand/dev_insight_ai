import requests

def analyze_repo(repo_url):
    repo_path = repo_url.split("github.com/")[-1].strip("/")
    api_base = f"https://api.github.com/repos/{repo_path}"

    # Get basic repo info
    repo_info = requests.get(api_base).json()
    issues = requests.get(f"{api_base}/issues").json()

    # Try to fetch README.md (default branch is usually 'main' or 'master')
    readme_url = f"https://raw.githubusercontent.com/{repo_path}/main/README.md"
    readme_response = requests.get(readme_url)

    if readme_response.status_code != 200:
        # Try 'master' if 'main' doesn't exist
        readme_url = f"https://raw.githubusercontent.com/{repo_path}/master/README.md"
        readme_response = requests.get(readme_url)

    readme = readme_response.text if readme_response.status_code == 200 else "README not found."

    return {
        "name": repo_info.get("name"),
        "description": repo_info.get("description"),
        "stars": repo_info.get("stargazers_count"),
        "language": repo_info.get("language"),
        "open_issues": len(issues),
        "topics": repo_info.get("topics", []),
        "readme": readme
    }
