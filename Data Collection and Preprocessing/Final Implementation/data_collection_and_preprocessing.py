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


class DataCollectionAndPreprocessing():
    """
    Class to automate and streamline data
    """

    def __init__(self):
        pass

    def invoke_scrapy(self):
        pass

    def convert_folder_to_csv(self):
        pass

    def clean_csv(self):
        pass

    def locationFromText(self):
        pass

    def locationUsingAPI(self):
        pass

    def mediaDownload(self):
        pass
