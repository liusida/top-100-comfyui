import os
import base64
import requests
import yaml
import time
from dotenv import load_dotenv

from utils.common import valid_filename

# Load the GitHub token from the .env file
load_dotenv()
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

with open('all_nodes.yml', 'r') as file:
    all_nodes = yaml.safe_load(file) # TODO: need to adjust based on the changed format

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

node_number_processed_each_time = 20 #

for node in all_nodes:
    if os.path.exists(f'node_examples/{valid_filename(node)}.md'):
        continue
    if node_number_processed_each_time <= 0: # too many requests, so each time we only process this many nodes.
        break
    node_number_processed_each_time -= 1

    search_query = f'{node} last_node_id last_link_id in:file extension:json'
    response = fetch_github_data(search_query, headers)
    while handle_api_rate_limit(response):
        response = fetch_github_data(search_query, headers)
    
    if response.status_code == 200:
        results = response.json()
        matching_items = []
        print(f"\n\n{node} hit {len(results.get('items', []))}")
        time.sleep(1)
        for item in results.get('items', []):
            file_url = item['url']
            print(".", end=" ", flush=True)
            
            file_response = requests.get(file_url, headers=headers)
            if file_response.status_code == 200:
                file_content_base64 = file_response.json().get('content')
                if file_content_base64:
                    file_content = base64.b64decode(file_content_base64).decode('utf-8')
                    if f'"type": "{node}"' in file_content:
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
        with open(f'node_examples/{valid_filename(node)}.md', 'w', encoding='utf-8') as f:
            f.write(f"# Here are {len(matching_items)} workflows that contain the node {node}:\n\n")
            for index, item in enumerate(matching_items):
                f.write(f"## {index+1}. \n\n")
                f.write(f"Size: {item['size']} bytes\n\n")
                f.write(f"URL: {item['url']}\n\n")
            all_nodes[node] = len(matching_items)
    else:
        if not handle_api_rate_limit(response):
            print(f"Failed to retrieve results: {response.status_code}")
            print(response.json())

# Write the updated dictionary back to the YAML file
with open('all_nodes.yml', 'w') as file:
    yaml.dump(all_nodes, file, default_flow_style=False)
