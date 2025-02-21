from scripts.crawl_info import get_crawl_indexes, query_common_crawl

if __name__ == '__main__':
    crawl = get_crawl_indexes()
    if crawl:
        result = query_common_crawl(crawl)
        for idx, result in enumerate(query_common_crawl(crawl) or [], 1):
            print(
                f'\n[{idx}º Resultado]'
                f'\nURL: {result['url']}'
                f'\nData: {result['timestamp']}'
                f'\nArquivo WARC: {result['filename']}'
            )
