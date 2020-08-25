import time
import threading
import multiprocessing
import os
import random
import subprocess
import shutil
import glob
import subprocess
from scrapy.crawler import CrawlerProcess
from TweetScraper.spiders import TweetCrawler as t
from scrapy.utils.project import get_project_settings

search_terms_data = []
with open("Data Gathered/Search_terms_data/cleanKeywords.txt", "r", encoding="utf-8") as f:
    search_terms_data = [x.strip() for x in f.readline().split(",")]

"""
Threading attempt starts here
"""

process = CrawlerProcess(get_project_settings())

"""
Threading Attempt ends here
"""

"""
Linear Approach works fine
"""

search_terms_data = search_terms_data[:2000]

for term in search_terms_data:
    process.crawl(t.TweetScraperClass, query=term,
                  lang="eng", crawl_user=True)
    time.sleep(0.1)

process.start()
print("complete")
