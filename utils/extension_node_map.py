import requests

extension_map = {}
EXTENSION_NODE_MAP_URL = "https://raw.githubusercontent.com/ltdrdata/ComfyUI-Manager/main/extension-node-map.json"

response = requests.get(EXTENSION_NODE_MAP_URL)
response.raise_for_status()
extension_map = response.json()
