import time
import threading
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
with open("Search_terms_data/Pandemic.txt", "r") as f:
    search_terms_data = f.readline().split(",")


"""
Threading attempt starts here
"""


def partition(list_in, n):
    random.shuffle(list_in)
    return [list_in[i::n] for i in range(n)]


split_data = partition(search_terms_data, 200)

split_1 = split_data[0]
split_2 = split_data[1]
split_3 = split_data[2]


process = CrawlerProcess(get_project_settings())


# def thread_1():
#     i = i.lstrip()
#     process.crawl(t.TweetScraperClass, query=i, lang="eng")

#     print(tweet_files)


# def thread_2():
#     tweet_files = {}
#     user_files = {}
#     for i in split_2:
#         i = i.lstrip()
#         process.crawl(t.TweetScraperClass, query=i, lang="eng")

#     print(tweet_files)


# def thread_3():
#     tweet_files = {}
#     user_files = {}
#     for i in split_3:
#         i = i.lstrip()
#         process.crawl(t.TweetScraperClass, query=i, lang="eng")

#     print(tweet_files)


# t2 = threading.Thread(target=thread_2, args=(10,))
# t1 = threading.Thread(target=thread_1)
# t2 = threading.Thread(target=thread_2)
# t3 = threading.Thread(target=thread_3)
# # t2.start()
# thread_1()

"""
Threading Attempt ends here
"""

"""
Linear Approach works fine
"""
for term in search_terms_data:
    process.crawl(t.TweetScraperClass, query=term, lang="eng", crawl_user=True)

process.start()
print("complete")
