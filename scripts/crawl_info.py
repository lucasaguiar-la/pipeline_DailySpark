import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_crawl_indexes():
    index_url = os.getenv('INDEX_URL')

    try:
        response = requests.get(index_url)
        response.raise_for_status()
        data = response.json()

    except requests.exceptions.HTTPError as e:
        print(f'Algo deu errado: {e}')
        return None

    return data

def get_crawl_segments(crawl_id):
    base_url = os.getenv('BASE_URL')
    segments_url = (f'{base_url}{crawl_id}-index')
    params = {
        'url': 'example.com', 
        'output': 'json'
    }
    try:
        response = requests.get(segments_url, params=params)
        response.raise_for_status()

    except requests.exceptions.HTTPError as e:
        print(f'Algo deu errado: {e}')
        return None

    return response.text.splitlines()
