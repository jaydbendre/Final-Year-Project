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
with open("Search_terms_data/Drought.txt", "r") as f:
    search_terms_data = f.readline().split(",")

"""
Threading attempt starts here
"""


def partition(list_in, n):
    random.shuffle(list_in)
    return [list_in[i::n] for i in range(n)]


split_data = partition(search_terms_data, 3)


process = CrawlerProcess(get_project_settings())


# def crawling_terms(list_of_terms, lock):
#     lock.acquire()
#     for term in list_of_terms:
#         term = term.lstrip()
#         process.crawl(t.TweetScraperClass, query=term,
#                       lang="eng", crawl_user=True)

#     lock.release()


# # if __name__ == '__main__':
# lock = threading.Lock()
# # p1 = multiprocessing.Process(
# #     target=crawling_terms, args=(split_data[0], lock))
# # p2 = multiprocessing.Process(
# #     target=crawling_terms, args=(split_data[1], lock))
# # p3 = multiprocessing.Process(
# #     target=crawling_terms, args=(split_data[2], lock))

# p1 = threading.Thread(
#     target=crawling_terms, args=(split_data[0], lock))
# p2 = threading.Thread(
#     target=crawling_terms, args=(split_data[1], lock))
# p3 = threading.Thread(
#     target=crawling_terms, args=(split_data[2], lock))

# p1.start()
# p2.start()
# p3.start()
# p1.join()
# p2.join()
# p3.join()

# print("Complete")
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
program_starts = time.time()

for term in search_terms_data:
    process.crawl(t.TweetScraperClass, query=term,
                  lang="eng", crawl_user=True)
# now = time.time()
# print(now)
#     if now - program_starts > 3600:
#         break

process.start()
print("complete")
