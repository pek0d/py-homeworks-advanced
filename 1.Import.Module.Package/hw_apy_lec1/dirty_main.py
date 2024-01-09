from icrawler.builtin import *
from icrawler.builtin import GoogleImageCrawler

google_crawler = GoogleImageCrawler(storage={"root_dir": "/Users/mark/Downloads"})

if __name__ == "__main__":
    google_crawler.crawl(keyword="cat", max_num=10)
