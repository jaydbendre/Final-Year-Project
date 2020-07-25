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
# from twisted.internet import reactor
# from scrapy.crawler import Crawler
# from scrapy.settings import Settings
# from .spiders import TweetCrawler
search_terms_data = []
with open("Search_terms_data/Pandemic.txt", "r") as f:
    search_terms_data = f.readline().split(",")

global_path = "Data Collection/Pandemic/"

print(len(search_terms_data))


def partition(list_in, n):
    random.shuffle(list_in)
    return [list_in[i::n] for i in range(n)]


split_data = partition(search_terms_data, 50)

split_1 = split_data[0]
split_2 = split_data[1]
split_3 = split_data[2]

# os.mkdir("Data Collection/Pandemic", 0o666)


def thread_1():
    process = CrawlerProcess(get_project_settings())
    tweet_files = {}
    user_files = {}
    for i in split_1:
        i = i.lstrip()
        process.crawl(t.TweetScraperClass, query=i, lang="eng",
                      tweet_location="Data/{}/tweets".format(i), user_location="Data/{}/user".format(i))
        # time.sleep(1000)
        tweet_file = glob.glob("Data/{}/tweet/*".format(i))
        user_file = glob.glob("Data/{}/user/*".format(i))
        tweet_files[i] = [f for f in tweet_file]
        user_files[i] = [f for f in user_file]
        mode = 0o666
        # if os.path.exists("{}/{}".format(global_path, i)):
        #     pass
        # else:
        #     os.mkdir("{}/{}".format(global_path, i), mode)
        #     tweet_path = "{}/{}/tweets".format(global_path, i)
        #     user_path = "{}/{}/users".format(global_path, i)

        #     os.mkdir(tweet_path, mode)
        #     os.mkdir(user_path, mode)
        # except FileExistsError:
        #     pass

        # for tweet in tweet_files:
        #     print(tweet)
        #     shutil.move(tweet, tweet_path)

        # for user in user_files:
        #     shutil.move(user, user_path)

        # shutil.rmtree("Data")
    process.start()
    # for k, v in tweet_files:
    #     print(k, "\t", len(v))
    # for k, v in user_files:
    #     print(k, "\t", len(v))
    print(tweet_files)

# def thread_2(n):
#     for i in split_2:
#         os.system('cmd /k "cd ../TweetScraper"')
#         os.system('cmd /k "scrapy crawl TweetScraper -a query = {}"'.format(i))
#         time.sleep(10000)
#         os.system('cmd /k "^c"')


# t2 = threading.Thread(target=thread_2, args=(10,))

# t2.start()
thread_1()
print("Thread 1")
# t2.join()
print("Thread 2")

print("complete")
