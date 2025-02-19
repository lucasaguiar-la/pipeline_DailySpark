from scripts.crawl_info import get_crawl_indexes, get_crawl_segments

if __name__ == '__main__':
    crawls = get_crawl_indexes()
    if crawls:
        print(f'Crawls disponíveis ({len(crawls)}):')
        for idx, crawl in enumerate(crawls[:5]):
            print(f'{idx + 1} - {crawl['name']}')
        
        option = int(input('\nEscolha o número do crawl que deseja explorar: ')) -1
        selected_option = crawls[option]

        print(
            f'\nExplorando crawl: {selected_option['name']}'
            f'ID: {selected_option['id']}'
            )
        
        print('\nBuscando segmentos...')
        segments = get_crawl_segments(crawl_id=selected_option['id'])
        if segments:
            for segment in segments[:5]:
                print(segments)
