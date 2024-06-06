import os
import requests
from datetime import datetime, timedelta, timezone
import pickle
from dotenv import load_dotenv

CACHE_FILE = 'repo_cache.pkl'
CACHE_EXPIRATION = timedelta(days=1)

def is_cache_valid():
    if not os.path.exists(CACHE_FILE):
        return False
    cache_mod_time = datetime.fromtimestamp(os.path.getmtime(CACHE_FILE))
    return datetime.now() - cache_mod_time < CACHE_EXPIRATION

def load_cache():
    with open(CACHE_FILE, 'rb') as f:
        return pickle.load(f)

def save_cache(repositories):
    with open(CACHE_FILE, 'wb') as f:
        pickle.dump(repositories, f)

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
    if is_cache_valid():
        repositories = load_cache()
    else:
        QUERY = "comfyui fork:true"
        PARAMS = {
            'q': QUERY,
            'sort': 'stars',
            'order': 'desc',
            'per_page': 100
        }    
        print(f"Getting all repositories ...")
        response = requests.get(SEARCH_URL, headers=HEADERS, params=PARAMS)
        response.raise_for_status()
        repositories = response.json().get('items', [])
        for repo in repositories:
            repo['last_commit'] = fetch_last_commit_date(repo['full_name'])
        save_cache(repositories)

    return repositories

def fetch_broader_repositories():
    QUERY = "(comfyui in:readme OR comfyui in:description OR comfyui in:topic) fork:true"
    PARAMS = {
        'q': QUERY,
        'sort': 'stars',
        'order': 'desc',
        'per_page': 100
    }
    print(f"Getting all a broader collection ...")
    response = requests.get(SEARCH_URL, headers=HEADERS, params=PARAMS)
    response.raise_for_status()
    repositories = response.json().get('items', [])
    return repositories