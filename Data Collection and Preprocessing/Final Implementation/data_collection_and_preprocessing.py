import glob
import time
import datetime
import os
import random
import json
import requests
import base64
import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
from scrapy.crawler import CrawlerProcess
from TweetScraper.spiders import TweetCrawler as t
from scrapy.utils.project import get_project_settings
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize


class DataCollectionAndPreprocessing():
    """
    Class to automate and streamline data
    """

    """
    Constructor to initialise variables
    """

    def __init__(self):
        pass

    """
    Get bearer token authorisation using Twitter API credentials
    """

    def authorise_API(self):
        creds = dict()
        with open("../../ourTwitterCred.json", "r") as f:
            creds = json.load(f)

        key_secret = "{}:{}".format(
            creds["api_key"], creds["api_secret"]).encode("ascii")

        b64_encoded_key = base64.b64encode(key_secret)
        b64_encoded_key = b64_encoded_key.decode("ascii")

        base_url = "https://api.twitter.com/"
        auth_url = "{}oauth2/token".format(base_url)

        auth_headers = {
            "Authorization": "Basic {}".format(b64_encoded_key),
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
        }

        auth_data = {
            "grant_type": "client_credentials"
        }

        auth_resp = requests.post(
            auth_url, headers=auth_headers, data=auth_data)

        return auth_resp

    """
    Deploy Scrapy to store data into folders inside /Data Gathered/Data
    """

    def invoke_scrapy(self):
        search_terms = list()
        with open("cleanKeywords.txt", "r") as f:
            search_terms = [x.strip() for x in f.readline().split(",")]

        process = CrawlerProcess(get_project_settings())

        for s in search_terms:
            process.crawl(t.TweetScraperClass, query=s,
                          lang="eng", crawl_user=True)
            time.sleep(1)

        process.start()

    """
    Convert collected data from folders to an aggregated CSV
    """

    def convert_folder_to_csv(self):
        folder_path = "../Data Gathered/Data/*"
        folders = glob.glob(folder_path)

        aggregated_data = list()
        for folder in folders:
            if folder == "Data/user":
                continue

            files = glob.glob(folder + "/tweets/*")

            for file in files:
                data = dict()

                with open(file, "r", encoding="utf-8") as f:
                    data = json.loads(f.read())
                    data["searched_by"] = folder.split("/")[2].capitalize()[5:]
                    aggregated_data.append(data)

        df = pd.DataFrame(aggregated_data)
        df = df.replace({"\n": " "}, regex=True)
        df = df.replace({"\t": " "}, regex=True)
        df = df.replace({"\r": " "}, regex=True)

        df.sort_values("datetime", ascending=True,
                       inplace=True, na_position="last")

        with open("../Data Gathered/{}.csv".format(datetime.datetime.now().date()), "w", encoding="utf-8") as file:
            df.to_csv(file, index=False)

    def clean_csv(self):
        pass

    def locationFromText(self, df):
        st = StanfordNERTagger('./NER Parser/stanford-ner-4.0.0/classifiers/english.all.3class.distsim.crf.ser.gz',
                       './stanford-ner-4.0.0/stanford-ner.jar', encoding='utf-8')

        # Assigning df['location_from_text'] with empty
        df['location_from_text'] = np.nan

        # Getting the Tweet content
        text_arr = df[['text']].values.tolist()
        
        location_arr = df[['location_from_text']].values.tolist()

        # Extracting Locations from Tweet Text
        for num,text in enumerate(text_arr):
            locations = ''
            temp = [ i.capitalize() for i in text.split(' ')]
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

        return df

    """
    Getting exact coordinates using Geopy and twitter api
    """

    def locationUsingAPI(self, df):
        auth_request = self.authorise_API()

        if auth_request.status_code == 200:
            access_token = auth_request.json()["access_token"]

            search_headers = {
                "Authorization": "Bearer {}".format(access_token)
            }

            twitter_id = df["ID"]

            search_url = "https://api.twitter.com/1.1/statuses/show.json"
            geolocator = Nominatim(user_agent="Soulage")
            for id in twitter_id:
                search_parameters = {
                    "id": str(id)
                }

                search_request = requests.get(
                    search_url,
                    headers=search_headers,
                    params=search_parameters
                )

                if search_request.status_code == 200:
                    data = search_request.json()

                    key = str(id)
                    if data[key]["geo"] == None and data[key]["place"] == None and data[key]["coordinates"] == None:
                        user_location = data[key]["user"]["location"]
                        if user_location == "":
                            df[df["ID"] == id]["location"] = np.NaN
                        else:
                            df[df["ID"] == id]["location"] = user_location
                            coords = geolocator.geocode(
                                df[df["ID"] == id]["location"])
                            df[df["ID"] == id]["coordinates"] = (
                                coords.latitude, coords.longitude)
                    else:
                        if data[key]["place"] == None:
                            df[df["ID"] == id]["location"] = np.NaN
                        else:
                            df[df["ID"] ==
                                id]["location"] = data[key]["place"]["full_name"]
                            coords = geolocator.geocode(
                                df[df["ID"] == id]["location"])
                            df[df["ID"] == id]["coordinates"] = (
                                coords.latitude, coords.longitude)
                else:
                    for i in range(300):
                        print("Waiting for {} seconds".format(300-i))
                        time.sleep(1)
            return df
        else:
            print("Not Authorised")
            return np.Nan

    def mediaDownload(self, df):
        pass
