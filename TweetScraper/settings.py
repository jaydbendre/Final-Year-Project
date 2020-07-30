# -*- coding: utf-8 -*-

# !!! # Crawl responsibly by identifying yourself (and your website/e-mail) on the user-agent
USER_AGENT = "D20-new-new (jaybendre123@gmail.com)"

# settings for spiders
BOT_NAME = 'Twitter Scraper for D-20(new new new)'
LOG_LEVEL = 'INFO'
# from http://stackoverflow.com/a/31233576/2297751, TODO
DOWNLOAD_HANDLERS = {'s3': None, }
DOWNLOAD_DELAY = 2
SPIDER_MODULES = ['TweetScraper.spiders']
NEWSPIDER_MODULE = 'TweetScraper.spiders'
ITEM_PIPELINES = {
    'TweetScraper.pipelines.SaveToFilePipeline': 100,
    # 'TweetScraper.pipelines.SaveToMongoPipeline':100, # replace `SaveToFilePipeline` with this to use MongoDB
    # 'TweetScraper.pipelines.SavetoMySQLPipeline':100, # replace `SaveToFilePipeline` with this to use MySQL
}

# settings for where to save data on disk
SAVE_TWEET_PATH = './Data/tweet/'
SAVE_USER_PATH = './Data/user/'

# settings for mongodb
MONGODB_SERVER = "127.0.0.1"
MONGODB_PORT = 27017
MONGODB_DB = "TweetScraper"        # database name to save the crawled data
MONGODB_TWEET_COLLECTION = "tweet"  # collection name to save tweets
MONGODB_USER_COLLECTION = "user"   # collection name to save users

# settings for mysql
MYSQL_SERVER = "127.0.0.1"
MYSQL_DB = "TweetScraper"
MYSQL_TABLE = "scraper"  # the table will be created automatically
# MySQL user to use (should have INSERT access granted to the Database/Table
MYSQL_USER = ""
MYSQL_PWD = ""        # MySQL user's password

CLOSESPIDER_TIMEOUT = 120
CLOSESPIDER_PAGECOUNT = 5

TELNETCONSOLE_ENABLED = False
ROBOTSTXT_OBEY = False
