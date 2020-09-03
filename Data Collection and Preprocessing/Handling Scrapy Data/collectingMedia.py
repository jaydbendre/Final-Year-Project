import requests
import json
import base64
import pandas as pd
import numpy as np


class MediaExtracter():

    def __init__(self):
        self.access_token = ""
        self.base_url = "https://api.twitter.com/labs/2/tweets/"

    # def authorise(self):
    #     creds = dict()
    #     with open('../TwitterCred.json', "r") as f:
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

    def mediaCollector(self):
        # auth_resp = self.authorise()

        # if auth_resp.status_code != 200:
        #     print("Error In getting the Bearer Token....")
        #     return

        # self.access_token = auth_resp.json()['access_token']
        data = dict()
        with open("../TwitterCred.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        self.access_token = data["BEARER_TOKEN"]
        request_headers = {
            "Authorization": "Bearer {}".format(self.access_token)
        }

        twitter_data = pd.DataFrame(pd.read_csv(
            "../Data Gathered/CollectedData.csv"))

        tweet_id = 1297759418969468928

        parameters = "?expansions=attachments.poll_ids,attachments.media_keys,author_id,entities.mentions.username,geo.place_id,in_reply_to_user_id,referenced_tweets.id,referenced_tweets.id.author_id&media.fields=duration_ms,height,media_key,preview_image_url,type,url,width,public_metrics,non_public_metrics,organic_metrics,promoted_metrics&place.fields=contained_within,country,country_code,full_name,geo,id,name,place_type"
        complete_url = self.base_url + \
            str(tweet_id) + parameters

        resp = requests.get(complete_url, headers=request_headers)
        retrieved_data = resp.json()

        with open("data_obtained.json", "w", encoding="utf-8") as f:
            json.dump(retrieved_data, f)


obj = MediaExtracter()
obj.mediaCollector()
