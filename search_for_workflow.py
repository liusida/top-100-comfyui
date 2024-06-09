import os
import base64
import requests
import yaml
import time
from dotenv import load_dotenv

# Load the GitHub token from the .env file
load_dotenv()
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

with open('all_nodes.yml', 'r') as file:
    all_nodes = yaml.safe_load(file)

def fetch_github_data(search_query, headers):
    # GitHub API endpoint for code search
    url = 'https://api.github.com/search/code'
    params = {'q': search_query, 'per_page': 100}
    response = requests.get(url, headers=headers, params=params)
    return response

def handle_api_rate_limit(response):
    if response.status_code == 403:
        print("Rate limit exceeded, sleeping for 60 seconds...")
        time.sleep(60)  # Sleep for 60 seconds
        return True
    return False

headers = {'Authorization': f'token {GITHUB_TOKEN}', 'Accept': 'application/vnd.github.v3+json'}

for node in all_nodes:
    search_query = f'{node} last_node_id last_link_id in:file extension:json'
    response = fetch_github_data(search_query, headers)
    while handle_api_rate_limit(response):
        response = fetch_github_data(search_query, headers)
    
    if response.status_code == 200:
        results = response.json()
        matching_items = []
        for item in results.get('items', []):
            file_url = item['url']
            file_response = requests.get(file_url, headers=headers)
            if file_response.status_code == 200:
                file_content_base64 = file_response.json().get('content')
                if file_content_base64:
                    file_content = base64.b64decode(file_content_base64).decode('utf-8')
                    if f'"{node}"' in file_content:
                        matching_items.append({
                            'repository': item['repository']['full_name'],
                            'name': item['name'],
                            'path': item['path'],
                            'url': item['html_url'],
                            'size': len(file_content)
                        })
            else:
                if handle_api_rate_limit(file_response):
                    continue  # If rate limit exceeded during file fetch, continue without adding

        matching_items.sort(key=lambda x: x['size'])
        os.makedirs('node_examples', exist_ok=True)
        with open(f'node_examples/{node}.md', 'w', encoding='utf-8') as f:
            for index, item in enumerate(matching_items):
                f.write(f"## {index+1}. \n\n")
                f.write(f"Size: {item['size']} bytes\n\n")
                f.write(f"URL: {item['url']}\n\n")
    else:
        if not handle_api_rate_limit(response):
            print(f"Failed to retrieve results: {response.status_code}")
            print(response.json())
