import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

def get_crawl_indexes():
    index_url = os.getenv('INDEX_URL')

    try:
        response = requests.get(url=index_url, timeout=10)
        response.raise_for_status()
        data = response.json()

        limit = 5
        options = []
        for option in data:
            if len(options) >= limit:
                break
            options.append(option['id'])

    except requests.exceptions.HTTPError as e:
        print(f'Algo deu errado ao carregar os índices: {e}')
        return None

    return options

def query_common_crawl(crawl_id, keyword=None, limit=5):
    base_url = os.getenv('BASE_URL')
    segments_url = (f'{base_url}{crawl_id}-index')
    params = {
        'url': os.getenv('DOMAIN_URL'), 
        'output': 'json'
    }
    try:
        response = requests.get(segments_url, params=params)
        response.raise_for_status()

        results = []
        for line in response.text.splitlines():
            if len(results) >= limit:
                break
            result = json.loads(line)

            if keyword and keyword.lower() not in result.get('url', '').lower():
                continue

            results.append(result)

    except requests.exceptions.HTTPError as e:
        print(f'Algo deu errado na query: {e}')
        return None

    return results
