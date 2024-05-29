import requests
import os
import pickle
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
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
    return response.json().get('items', [])

def load_cache():
    with open(CACHE_FILE, 'rb') as f:
        return pickle.load(f)

def save_cache(repositories):
    with open(CACHE_FILE, 'wb') as f:
        pickle.dump(repositories, f)

def main():
    if is_cache_valid():
        repositories = load_cache()
        print("Loaded repositories from cache.")
    else:
        repositories = fetch_repositories()
        save_cache(repositories)
        print("Fetched and cached new repositories.")

    print(f"Got {len(repositories)} repositories.")
    
    # Get the current date
    current_date = datetime.now().strftime('%Y-%m-%d')

    with open("README.md", "w", encoding="utf-8") as f:
        # Write the updated date at the beginning
        f.write("This repository automatically updates a list of the top 100 repositories related to ComfyUI based on the number of stars on GitHub.\n\n")
        f.write(f"### Last updated: {current_date}\n\n")

        for i in range(0, len(repositories), 5):
            f.write(f"# TOP {i+1} - {i+5}\n\n")
            repo_group = repositories[i:i + 5]
            repo_names = [repo['full_name'] for repo in repo_group]
            repo_urls = [f"https://github.com/{name}" for name in repo_names]
            star_counts = [repo['stargazers_count'] for repo in repo_group]
            avatar_urls = [repo['owner']['avatar_url'] for repo in repo_group]
            descriptions = [repo['description'] for repo in repo_group]
            
            for j, (repo_name, repo_url, star_count, avatar_url, description) in enumerate(zip(repo_names, repo_urls, star_counts, avatar_urls, descriptions)):
                if star_count < 1000:
                    str_star_count = f"{star_count}"
                else:
                    str_star_count = f"{star_count / 1000:.1f}k"
                f.write(f"## {i+j+1}. {repo_name}\n\n")
                f.write(f"<a href='{repo_url}'><img src=\"{avatar_url}\" alt=\"Owner Avatar\" width=\"50\" height=\"50\"></a> &nbsp; &nbsp; {repo_url}\n\n")
                f.write(f"**Stars**: {str_star_count}\n\n")
                f.write(f"{description}\n\n")
            
            chart_url = f"https://api.star-history.com/svg?repos={','.join(repo_names)}&type=Date"
            f.write(f'<a href="https://star-history.com/#{",".join(repo_names)}&Date"><img src="{chart_url}" alt="Star History Chart" width="600"></a>\n\n')

if __name__ == "__main__":
    main()
