import itertools
import requests
import os
import yaml
from datetime import datetime, timedelta, timezone

from utils.github import GITHUB_TOKEN, fetch_repositories
from utils.extension_node_map import extension_map, EXTENSION_NODE_MAP_URL
from utils.common import format_updated_at_date, load_template, get_human_readable_star_count
from utils.pickle_cache import is_cache_valid, load_cache, save_cache

def get_extension_nodes(repo_url):
    ret = ""
    nodes = extension_map.get(repo_url, [])
    if nodes:
        nodes_sorted = sorted(nodes[0], key=str.casefold)
        grouped_nodes = itertools.groupby(nodes_sorted, key=lambda x: x[0].upper())
        ret += f"<details><summary>Included Nodes ({len(nodes[0])}){'?' if len(nodes[0]) == 0 else ''}</summary>\n\n"
        if (len(nodes[0])):
            for key, group in grouped_nodes:
                ret += " - " + ", ".join(group) + "\n"
        else:
            ret += " - Sorry, we can't get the node list for this project since it lacks conventional `NODE_CLASS_MAPPINGS` and doesn't have a `node_list.json` file to specify the node details according to [ComfyUI-Manager's support guide](https://github.com/ltdrdata/ComfyUI-Manager#custom-node-support-guide)"
        ret += "</details>\n\n"
    return ret

def load_tags(file_path='tags.yml'):
    with open(file_path, 'r', encoding="utf-8") as file:
        return yaml.safe_load(file)

def write_tag_file(tag, repositories, tags):
    tag_filename = f"tags/{tag.replace(' ', '')}.md"
    os.makedirs(os.path.dirname(tag_filename), exist_ok=True)
    with open(tag_filename, "w", encoding="utf-8") as f:
        f.write(f"# Repositories tagged with `{tag}`\n\n")
        for repo in repositories:
            repo_url = f"https://github.com/{repo['full_name']}"
            str_star_count = get_human_readable_star_count(repo['stargazers_count'])
            avatar_url = repo['owner']['avatar_url']
            description = repo['description']
            updated_at = repo['updated_at']
            repo_item = load_template("repo_item").render({
                "repo_name": repo['full_name'],
                "repo_url": repo_url,
                "avatar_url": avatar_url,
                "star_count": str_star_count,
                "created_at": format_updated_at_date(updated_at),
                "description": description,
            })
            f.write(repo_item)
            extension_nodes = get_extension_nodes(repo_url)
            f.write(extension_nodes)
            
def write_by_date_file(repositories, tags):
    sorted_repos = sorted(repositories, key=lambda x: x['created_at'])
    with open("byDate.md", "w", encoding="utf-8") as f:
        f.write("## Repositories ordered by creation date (oldest to newest)\n\n")
        for repo in sorted_repos:
            repo_url = f"https://github.com/{repo['full_name']}"
            str_star_count = get_human_readable_star_count(repo['stargazers_count'])
            avatar_url = repo['owner']['avatar_url']
            description = repo['description']
            created_at = repo['created_at']
            repo_tags = tags.get(repo['full_name'], [])
            repo_item = load_template("repo_item").render({
                "repo_name": repo['full_name'],
                "repo_url": repo_url,
                "avatar_url": avatar_url,
                "star_count": str_star_count,
                "created_at": format_updated_at_date(created_at),
                "tags": ' '.join([f'`{tag}`' for tag in repo_tags]),
                "description": description,
            })
            f.write(repo_item)

            extension_nodes = get_extension_nodes(repo_url)
            f.write(extension_nodes)

def write_readme_file(repositories, tags, tag_links, preview=False):
    filename = "README.md" if not preview else "README.preview.md"
    with open(filename, "w", encoding="utf-8") as f:
        header = load_template("header").render({
            "updated_date": datetime.now(timezone.utc).strftime('%Y-%m-%d'),
        })
        f.write(header)

        # Write links to the tag files
        f.write("### Repositories by Tag:\n")
        f.write("\n".join(tag_links) + "\n\n")

        for i in range(0, len(repositories), 5):
            f.write(f"# TOP {i+1} - {i+5}\n\n")
            repo_group = repositories[i:i + 5]
            repo_names = [repo['full_name'] for repo in repo_group]
            repo_urls = [f"https://github.com/{name}" for name in repo_names]
            star_counts = [repo['stargazers_count'] for repo in repo_group]
            avatar_urls = [repo['owner']['avatar_url'] for repo in repo_group]
            descriptions = [repo['description'] for repo in repo_group]
            updated_ats = [repo['updated_at'] for repo in repo_group]
            created_ats = [repo['created_at'] for repo in repo_group]

            star_history_url = f"https://api.star-history.com/svg?repos={','.join(repo_names)}&type=Date"
            f.write(f'<details><summary>Star History for TOP {i+1} - {i+5}</summary><a href="{star_history_url}"><img src="{star_history_url}" alt="Star History Chart" width="400"></a></details>\n\n')

            for j, (repo_name, repo_url, star_count, avatar_url, description, updated_at, created_at) in enumerate(zip(repo_names, repo_urls, star_counts, avatar_urls, descriptions, updated_ats, created_ats)):
                str_star_count = get_human_readable_star_count(star_count)
                # Get the tags for the current repository
                repo_tags = tags.get(repo_name, [])

                repo_item = load_template("repo_item").render({
                    "index": i+j+1,
                    "repo_name": repo_name,
                    "repo_url": repo_url,
                    "avatar_url": avatar_url,
                    "star_count": str_star_count,
                    "updated_at": format_updated_at_date(updated_at),
                    "created_at": format_updated_at_date(created_at),
                    "tags": ' '.join([f'`{tag}`' for tag in repo_tags]),
                    "description": description,
                })
                f.write(repo_item)

                extension_nodes = get_extension_nodes(repo_url)
                f.write(extension_nodes)


        footer = load_template("footer").render({
            "EXTENSION_NODE_MAP_URL": EXTENSION_NODE_MAP_URL,
            "updated_time": datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S %Z'),
        })
        f.write(footer)

# Create a dictionary to store repositories by tags
def get_repos_by_tag(repositories, tags):
    repos_by_tag = {}
    for repo in repositories:
        repo_name = repo['full_name']
        repo_tags = tags.get(repo_name, [])
        for tag in repo_tags:
            if tag not in repos_by_tag:
                repos_by_tag[tag] = []
            repos_by_tag[tag].append(repo)
    return repos_by_tag

# Create a list for tag links to show as kind of menu
def get_tag_links(repos_by_tag):
    tag_links = []
    # Collect tag names and their counts
    tag_counts = [(tag, len(repos)) for tag, repos in repos_by_tag.items()]

    # Sort tags by the number of repositories in descending order
    sorted_tag_counts = sorted(tag_counts, key=lambda x: x[1], reverse=True)

    # Create the links for each tag
    for tag, count in sorted_tag_counts:
        tag_links.append(f"- [{tag}](tags/{tag.replace(' ', '')}.md) ({count})")

    def move_tag(tag_links, tag_name, to_end=True):
        tag_to_move = next((link for link in tag_links if tag_name in link), None)
        if tag_to_move:
            tag_links.remove(tag_to_move)
            if to_end:
                tag_links.append(tag_to_move)
            else:
                tag_links.insert(0, tag_to_move)
        return tag_links
    
    # Reorder a bit
    tag_links = move_tag(tag_links, "Core", to_end=False)
    tag_links = move_tag(tag_links, "Chinese Language")
    tag_links = move_tag(tag_links, "Deprecated")
    return tag_links

def main():
    if is_cache_valid():
        repositories = load_cache()
    else:
        repositories = fetch_repositories()
        save_cache(repositories)

    tags = load_tags().get('tags', {})

    print(f"Got {len(repositories)} repositories.")

    # Create a dictionary to store repositories by tags
    repos_by_tag = get_repos_by_tag(repositories, tags)
    # Create a list for tag links to show as kind of menu
    tag_links = get_tag_links(repos_by_tag)
    
    # Write README.md file
    write_readme_file(repositories, tags, tag_links, preview=True)

    # Write individual tag files
    for tag, repos in repos_by_tag.items():
        write_tag_file(tag, repos, tags)
    
    # Write by date file
    write_by_date_file(repositories, tags)

if __name__ == "__main__":
    main()
