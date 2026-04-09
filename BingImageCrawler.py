!pip install icrawler

from icrawler.builtin import BingImageCrawler

keyword = input('검색어 입력: ')  # Modify with your desired search query
num_images = int(input('사진 몇장 크롤할까요?: '))  # Number of images to download (modify as needed)

crawler = BingImageCrawler(downloader_threads=4, storage={'root_dir': f'./{keyword}'})
crawler.crawl(keyword=keyword, max_num=num_images)

print ('Done!!')
