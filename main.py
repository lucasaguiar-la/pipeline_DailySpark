from scripts.crawl_info import get_crawl_indexes, query_common_crawl

if __name__ == '__main__':
    crawls = get_crawl_indexes()
    if crawls:
        for idx, crawl in enumerate(crawls):
            print(f'{idx + 1}º Crawl - {crawl}')
            result = query_common_crawl(crawl_id=crawl)
            if result:
                for idx, result in enumerate(result, 1):
                    print(
                        f'\n[{idx}º Resultado]'
                        f'\nURL: {result['url']}'
                        f'\nData: {result['timestamp']}'
                        f'\nArquivo WARC: {result['filename']}'
                    )
