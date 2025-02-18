import requests

def get_crawl_info():
    try:
        index_url = 'https://index.commoncrawl.org/collinfo.json'
        response = requests.get(index_url)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.HTTPError as e:
        print(f'Algo deu errado: {e}')
        return None
    except Exception as e:
        print(f'Outro erro ocorreu: {e}')
        return None
    return data
