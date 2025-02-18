from scripts.crawl_info import get_crawl_info

if __name__ == '__main__':
    crawls = get_crawl_info()
    if crawls:
        print(f'crawls disponíveis ({len(crawls)}):')
        for idx, crawl in enumerate(crawls[:3]):
            print(f'{idx + 1} - {crawl['name']}')