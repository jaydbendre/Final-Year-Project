import time
import threading
import os
import random
import subprocess
import shutil
import glob

search_terms_data = []
with open("../Search_terms_data/Pandemic.txt", "r") as f:
    search_terms_data = f.readline().split(",")

global_path = "../Data Collection/Pandemic/"

print(len(search_terms_data))


def partition(list_in, n):
    random.shuffle(list_in)
    return [list_in[i::n] for i in range(n)]


split_data = partition(search_terms_data, 3)

split_1 = split_data[0]
split_2 = split_data[1]
split_3 = split_data[2]

os.mkdir("../Data Collecction/Pandemic", 0o666)


def thread_1(n):
    for i in split_1:
        os.system(
            'scrapy crawl TweetScraper -a query={}"'.format(i))
        tweet_files = glob.glob("Data/tweet/*")
        user_files = glob.glob("Data/user/*")
        mode = 0o666
        os.mkdir("{}/{}".format(global_path, i), mode)
        tweet_path = "{}/{}/tweets".format(global_path, i)
        user_path = "{}/{}/users".format(global_path, i)

        os.mkdir(tweet_path, mode)
        os.mkdir(user_path, mode)

        for tweet in tweet_files:
            shutil.move(tweet, tweet_path)

        for user in user_files:
            shutil.move(user, user_path)

        os.rmdir("Data/tweet")
        os.rmdir("Data/user")

# def thread_2(n):
#     for i in split_2:
#         os.system('cmd /k "cd ../TweetScraper"')
#         os.system('cmd /k "scrapy crawl TweetScraper -a query = {}"'.format(i))
#         time.sleep(10000)
#         os.system('cmd /k "^c"')


t1 = threading.Thread(target=thread_1, args=(10,))
# t2 = threading.Thread(target=thread_2, args=(10,))

t1.start()
# t2.start()

t1.join()
print("Thread 1")
# t2.join()
print("Thread 2")

print("complete")
