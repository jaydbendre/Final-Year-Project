import glob
import time
import datetime
import os
import random
import json
import requests
import urllib.request
import base64
import pandas as pd
import numpy as np
import tweepy as tw
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
import threading


class DataCollectionAndPreprocessing():
    """
    Class to automate and streamline data
    """

    """
    Constructor to initialise variables
    """

    def __init__(self):
        self.api = ""
        pass

    """
    Data collection using tweepy
    """

    def collectingDataUsingApi(self):
        search_words = []
        with open("cleanKeywords.txt", "r", encoding="utf-8") as f:
            search_words = f.readline().split(",")

        # print(search_words)
        creds = dict()

        with open("TwitterCred.json", "r") as f:
            creds = dict(json.load(f))

        auth = tw.OAuthHandler(creds["api_key"], creds["api_secret"])
        auth.set_access_token(creds["access_token"],
                              creds["access_secret"])

        self.api = tw.API(auth, wait_on_rate_limit=True)

        threads = []
        for i in search_words:
            # print(i)
            t = threading.Thread(target=self.run_filter, args=(i,))
            t.start()
            threads.append(t)

    def run_filter(self, search_word):
        # print(search_word)
        stream = tw.Stream(
            auth=self.api.auth, listener=DataCollectionStreamListener(search_word, 15*60))

        stream.filter(track=[search_word], is_async=True)
        # time.sleep(5)

    pass
    """
    Convert collected data from folders to an aggregated CSV
    """

    def convert_folder_to_csv(self):

        parent_dir = "Data Gathered/"

        folders = glob.glob(parent_dir+"*")

        print(folders)

        data = []
        for folder in folders:
            files = glob.glob(folder+"/*")

            for file in files:
                json_string = open(file, "r", encoding="utf-8").read()
                json_dict = json.loads(json_string)

                filter_dict = {
                    "id": json_dict["id"],
                    "text": json_dict["text"],
                    "user_id": json_dict["user"]["id"],
                    "user_name": json_dict["user"]["name"],
                    "verfied": json_dict["user"]["verified"],
                    "geo": json_dict["geo"],
                    "quoted": json_dict["quote_count"],
                    "favorite": json_dict["favorite_count"],
                    "retweet": json_dict["retweet_count"],
                    "favorite": json_dict["favorite_count"],
                    "search_term": folder[14:]
                }

                if json_dict["place"] == None:
                    filter_dict["place"] = np.NaN
                    filter_dict["coordinates"] = np.NaN

                else:
                    filter_dict["place"] = json_dict["place"]["full_name"]
                    filter_dict["coordinates"] = (json_dict["place"]["bounding_box"]["coordinates"]
                                                  [0][0][0], json_dict["place"]["bounding_box"]["coordinates"][0][0][1])

                if "extended_tweet" in json_dict.keys():
                    media_data = json_dict["extended_tweet"]["entities"]
                    if "media" in media_data.keys():
                        filter_dict["media_type"] = json_dict["extended_tweet"]["entities"]["media"][0]["type"]
                        filter_dict["media_url"] = json_dict["extended_tweet"]["entities"]["media"][0]["media_url_https"]
                        filter_dict["media_id"] = json_dict["extended_tweet"]["entities"]["media"][0]["id"]
                    else:
                        filter_dict["media_type"] = np.NaN
                        filter_dict["media_url"] = ""
                        filter_dict["media_id"] = np.NaN
                else:
                    filter_dict["media_type"] = np.NaN
                    filter_dict["media_url"] = ""
                    filter_dict["media_id"] = np.NaN
                data.append(filter_dict)

        df = pd.DataFrame(data=data)
        # remove linebreaks in the dataframe
        df = df.replace({'\n': ' '}, regex=True)
        # remove tabs in the dataframe
        df = df.replace({'\t': ' '}, regex=True)
        # remove carriage return in the dataframe
        df = df.replace({'\r': ' '}, regex=True)

        old_df = pd.DataFrame(
            pd.read_csv("CollectedData.csv")
        )

        if len(old_df) == 0:
            df.to_csv("CollectedData.csv", index=False)
        else:
            df.to_csv("CollectedData.csv", index=False, mode="a", header=False)

    def clean_csv(self):
        df = pd.DataFrame(
            pd.read_csv(
                "CollectedData.csv"
            )
        )
        df.drop_duplicates(subset="text", keep="last", inplace=True)
        df["rt"] = df["text"].apply(self.identify_RT, 1)

    def locationFromText(self):
        df = pd.DataFrame(
            pd.read_csv("CollectedData.csv")
        )
        st = StanfordNERTagger('./NER Parser/stanford-ner-4.0.0/classifiers/english.all.3class.distsim.crf.ser.gz',
                               './NER Parser/stanford-ner-4.0.0/stanford-ner.jar', encoding='utf-8')

        # Assigning df['location_from_text'] with empty
        df['location_from_text'] = np.nan

        # Getting the Tweet content
        text_arr = df[['text']].values.tolist()

        location_arr = df[['location_from_text']].values.tolist()

        # Extracting Locations from Tweet Text
        for num,text in enumerate(text_arr):
            locations = ''
            temp = [i.capitalize() for i in text.split(' ')]
            text = ''
            for i in temp:
                text += (i + ' ')

            text = text[:-1]

            tokenized_text = word_tokenize(text)
            classified_text = st.tag(tokenized_text)

            for i in classified_text:
                if i[1] == 'LOCATION':
                    locations += i[0] + ","

            location_arr[num] = locations[:-1]
        
        # Assigning the location_from_text to dataframe
        df['location_from_text'] = location_arr
        print(location_arr)
        return df

    def mediaDownload(self, df):
        def media_helper(df):
            if df["media_type"] == np.NaN:
                return
            else:
                if os.path.isdir("Data Gathered/{}/media".format(df["search_term"])) == False:
                    os.makedirs(
                        "Data Gathered/{}/media".format(df["search_term"]))

                try:
                    if df["media_type"] == "photo":
                        urllib.request.urlretrieve(
                            df["media_url"], "Data Gathered/{}/media/{}.png".format(df["search_term"], df["id"]))
                    elif df["media_type"] == "video":
                        urllib.request.urlretrieve(
                            df["media_url"], "Data Gathered/{}/media/{}.png".format(df["search_term"], df["id"]))
                    elif df["media_type"] == "animated_gif":
                        urllib.request.urlretrieve(
                            df["media_url"], "Data Gathered/{}/media/{}.gif".format(df["search_term"], df["id"]))
                except urllib.error.HTTPError:
                    return
        df.apply(media_helper, 1)

    def identify_RT(self, item):
        if item.startswith("RT"):
            return True
        else:
            return False
        pass


class DataCollectionStreamListener(tw.StreamListener):

    def __init__(self, search_term, limit):
        super().__init__()
        self.search_term = search_term
        self.limit = limit
        self.start_time = time.time()

    def on_status(self, status):
        # print(status)
        if(time.time() - self.start_time) < self.limit:
            if os.path.isdir("Data Gathered") == False:
                os.mkdir("Data Gathered")

            if os.path.isdir("Data Gathered/{}".format(self.search_term)) == False:
                os.mkdir("Data Gathered/{}".format(self.search_term))

            parent_dir = "Data Gathered/{}/".format(self.search_term)
            with open(parent_dir+"{}.json".format(status.id), "w", encoding="utf-8") as f:
                json.dump(status._json, f)

            return True
        else:
            return False


DataCollectionAndPreprocessing().collectingDataUsingApi()
# DataCollectionAndPreprocessing().invoke_scrapy()
# DataCollectionAndPreprocessing().convert_folder_to_csv()
# DataCollectionAndPreprocessing().locationFromText()


"""
Get bearer token authorisation using Twitter API credentials
"""

# def authorise_API(self):
#     creds = dict()
#     with open("TwitterCred.json", "r") as f:
#         creds = json.load(f)

#     key_secret = "{}:{}".format(
#         creds["api_key"], creds["api_secret"]).encode("ascii")

#     b64_encoded_key = base64.b64encode(key_secret)
#     b64_encoded_key = b64_encoded_key.decode("ascii")

#     base_url = "https://api.twitter.com/"
#     auth_url = "{}oauth2/token".format(base_url)

#     auth_headers = {
#         "Authorization": "Basic {}".format(b64_encoded_key),
#         "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
#     }

#     auth_data = {
#         "grant_type": "client_credentials"
#     }

#     auth_resp = requests.post(
#         auth_url, headers=auth_headers, data=auth_data)

#     return auth_resp

"""
Deploy Scrapy to store data into folders inside /Data Gathered/Data
"""

# def invoke_scrapy(self):
#     search_terms = list()
#     with open("cleanKeywords.txt", "r") as f:
#         search_terms = [x.strip() for x in f.readline().split(",")]

#     process = CrawlerProcess(get_project_settings())

#     for s in search_terms:
#         process.crawl(t.TweetScraper, query=s)
#         # time.sleep(1)

#     process.start()

# """
# Getting exact coordinates using Geopy and twitter api
# """

# def locationUsingAPI(self, df):
#     auth_request = self.authorise_API()

#     if auth_request.status_code == 200:
#         access_token = auth_request.json()["access_token"]

#         search_headers = {
#             "Authorization": "Bearer {}".format(access_token)
#         }

#         twitter_id = df["ID"]

#         search_url = "https://api.twitter.com/1.1/statuses/show.json"
#         geolocator = Nominatim(user_agent="Soulage")
#         for id in twitter_id:
#             search_parameters = {
#                 "id": str(id)
#             }

#             search_request = requests.get(
#                 search_url,
#                 headers=search_headers,
#                 params=search_parameters
#             )

#             if search_request.status_code == 200:
#                 data = search_request.json()

#                 key = str(id)
#                 if data[key]["geo"] == None and data[key]["place"] == None and data[key]["coordinates"] == None:
#                     user_location = data[key]["user"]["location"]
#                     if user_location == "":
#                         df[df["ID"] == id]["location"] = np.NaN
#                     else:
#                         df[df["ID"] == id]["location"] = user_location
#                         coords = geolocator.geocode(
#                             df[df["ID"] == id]["location"])
#                         df[df["ID"] == id]["coordinates"] = (
#                             coords.latitude, coords.longitude)
#                 else:
#                     if data[key]["place"] == None:
#                         df[df["ID"] == id]["location"] = np.NaN
#                     else:
#                         df[df["ID"] ==
#                             id]["location"] = data[key]["place"]["full_name"]
#                         coords = geolocator.geocode(
#                             df[df["ID"] == id]["location"])
#                         df[df["ID"] == id]["coordinates"] = (
#                             coords.latitude, coords.longitude)
#             else:
#                 for i in range(300):
#                     print("Waiting for {} seconds".format(300-i))
#                     time.sleep(1)
#         return df
#     else:
#         print("Not Authorised")
#         return np.Nan
