import os
from datetime import datetime, timedelta, timezone
import pickle

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

