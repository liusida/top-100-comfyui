import os
import base64
import requests
import yaml
from dotenv import load_dotenv

# Load the GitHub token from the .env file
load_dotenv()
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

with open('all_nodes.yml', 'r') as file:
    all_nodes = yaml.safe_load(file)

for node in all_nodes:
    # Define the search parameters
    search_query = f'{node} last_node_id last_link_id in:file extension:json'

    # GitHub API endpoint for code search
    url = 'https://api.github.com/search/code'

    # Headers for authentication
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }

    # Parameters for the search query
    params = {
        'q': search_query,
        'per_page': 100  # Number of results per page (max is 100)
    }

    # Make the request to the GitHub API
    response = requests.get(url, headers=headers, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        results = response.json()
        print(f"hit {len(results.get('items', []))}")
        matching_items = []
        
        for item in results.get('items', []):
            # Fetch the file content to ensure exact match
            file_url = item['url']
            print(".", end=" ")
            file_response = requests.get(file_url, headers=headers)
            if file_response.status_code == 200:
                file_content_base64 = file_response.json().get('content')
                if file_content_base64:
                    # Decode the base64 content
                    file_content = base64.b64decode(file_content_base64).decode('utf-8')
                    # Check for exact match within the file content
                    if f'"{node}"' in file_content:
                        matching_items.append({
                            'repository': item['repository']['full_name'],
                            'name': item['name'],
                            'path': item['path'],
                            'url': item['html_url'],
                            'size': len(file_content)
                        })
            else:
                print(f"Failed to retrieve file content: {file_response.status_code}")

        # Sort matching items by file size
        matching_items.sort(key=lambda x: x['size'])

        # Write the results to a file
        os.makedirs('node_examples', exist_ok=True)
        with open(f'node_examples/{node}.md', 'w', encoding='utf-8') as f:
            for item in matching_items:
                f.write(f"Repository: {item['repository']}\n")
                f.write(f"File: {item['name']}\n")
                f.write(f"Path: {item['path']}\n")
                f.write(f"Size: {item['size']} bytes\n")
                f.write(f"URL: {item['url']}\n")
                f.write("-" * 80 + "\n")
    else:
        print(f"Failed to retrieve results: {response.status_code}")
        print(response.json())
