import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
if not GITHUB_TOKEN:
    raise ValueError("No GITHUB_TOKEN provided. Ensure it is set in your environment variables.")


HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3.star+json'
}
SEARCH_URL = "https://api.github.com/search/repositories"
QUERY = "comfyui fork:true"
PARAMS = {
    'q': QUERY,
    'sort': 'stars',
    'order': 'desc',
    'per_page': 100
}

def fetch_last_commit_date(repo_full_name):
    commits_url = f"https://api.github.com/repos/{repo_full_name}/commits"
    print(f"Getting {repo_full_name} ...")
    response = requests.get(commits_url, headers=HEADERS, params={'per_page': 1})
    response.raise_for_status()
    commits = response.json()
    if commits:
        return commits[0]['commit']['committer']['date']
    return None

def fetch_repositories():
    print(f"Getting all repositories ...")
    response = requests.get(SEARCH_URL, headers=HEADERS, params=PARAMS)
    response.raise_for_status()
    repositories = response.json().get('items', [])
    for repo in repositories:
        repo['last_commit'] = fetch_last_commit_date(repo['full_name'])
    return repositories