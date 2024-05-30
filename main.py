import requests
import os
import pickle
import yaml
from datetime import datetime, timedelta, timezone
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
QUERY = "comfyui"
PARAMS = {
    'q': QUERY,
    'sort': 'stars',
    'order': 'desc',
    'per_page': 100
}
CACHE_FILE = 'repo_cache.pkl'
CACHE_EXPIRATION = timedelta(days=1)

def is_cache_valid():
    if not os.path.exists(CACHE_FILE):
        return False
    cache_mod_time = datetime.fromtimestamp(os.path.getmtime(CACHE_FILE))
    return datetime.now() - cache_mod_time < CACHE_EXPIRATION

def fetch_repositories():
    response = requests.get(SEARCH_URL, headers=HEADERS, params=PARAMS)
    response.raise_for_status()
    repositories = response.json().get('items', [])
    for repo in repositories:
        repo['last_commit'] = fetch_last_commit_date(repo['full_name'])
    return repositories

def fetch_last_commit_date(repo_full_name):
    commits_url = f"https://api.github.com/repos/{repo_full_name}/commits"
    response = requests.get(commits_url, headers=HEADERS, params={'per_page': 1})
    response.raise_for_status()
    commits = response.json()
    if commits:
        return commits[0]['commit']['committer']['date']
    return None

def load_cache():
    with open(CACHE_FILE, 'rb') as f:
        return pickle.load(f)

def save_cache(repositories):
    with open(CACHE_FILE, 'wb') as f:
        pickle.dump(repositories, f)

def format_updated_at_date(date_str):
    date_obj = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
    return date_obj.strftime('%Y-%m-%d')

def load_tags(file_path='tags.yml'):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def main():
    if is_cache_valid():
        repositories = load_cache()
        print("Loaded repositories from cache.")
    else:
        repositories = fetch_repositories()
        save_cache(repositories)
        print("Fetched and cached new repositories.")

    tags = load_tags().get('tags', {})

    print(f"Got {len(repositories)} repositories.")
    
    with open("README.md", "w", encoding="utf-8") as f:
        # Write the updated date at the beginning
        f.write("This repository automatically updates a list of the top 100 repositories related to ComfyUI based on the number of stars on GitHub.\n\n")
        f.write(f"### Automatically updated on: {datetime.now(timezone.utc).strftime('%Y-%m-%d')}\n\n")

        for i in range(0, len(repositories), 5):
            f.write(f"# TOP {i+1} - {i+5}\n\n")
            repo_group = repositories[i:i + 5]
            repo_names = [repo['full_name'] for repo in repo_group]
            repo_urls = [f"https://github.com/{name}" for name in repo_names]
            star_counts = [repo['stargazers_count'] for repo in repo_group]
            avatar_urls = [repo['owner']['avatar_url'] for repo in repo_group]
            descriptions = [repo['description'] for repo in repo_group]
            updated_ats = [repo['updated_at'] for repo in repo_group]
            
            for j, (repo_name, repo_url, star_count, avatar_url, description, updated_at) in enumerate(zip(repo_names, repo_urls, star_counts, avatar_urls, descriptions, updated_ats)):
                if star_count < 1000:
                    str_star_count = f"{star_count}"
                else:
                    str_star_count = f"{star_count / 1000:.1f}k"
                
                # Get the tags for the current repository
                repo_tags = tags.get(repo_name, [])

                f.write(f"## {i+j+1}. {repo_name}\n\n")
                f.write(f"<a href='{repo_url}'><img src=\"{avatar_url}\" alt=\"Owner Avatar\" width=\"50\" height=\"50\"></a> &nbsp; &nbsp; {repo_url}\n\n")
                f.write(f"**Stars**: `{str_star_count}` | ")
                f.write(f"**Last updated**: `{format_updated_at_date(updated_at)}` | ")
                f.write(f"**Tags**: {' '.join([f'`{tag}`' for tag in repo_tags])}\n\n")
                f.write(f"{description}\n\n")
            
            chart_url = f"https://api.star-history.com/svg?repos={','.join(repo_names)}&type=Date"
            f.write(f'<a href="https://star-history.com/#{",".join(repo_names)}&Date"><img src="{chart_url}" alt="Star History Chart" width="600"></a>\n\n')

        f.write(f"### Automatically updated on: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S %Z')}\n\n")

if __name__ == "__main__":
    main()
