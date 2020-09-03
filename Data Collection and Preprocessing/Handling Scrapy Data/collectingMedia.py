import requests
import json
import base64
import pandas as pd
import numpy as np


class MediaExtracter():

    def __init__(self):
        self.access_token = ""
        self.base_url = "https://api.twitter.com/labs/2/tweets/"

    def authorise(self):
        creds = dict()
        with open('../TwitterCred.json', "r") as f:
            creds = json.load(f)

        key_secret = "{}:{}".format(creds["api_key"], creds["api_secret"]).encode("ascii")

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

        auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

        return auth_resp
    

    def mediaCollector(self):
        auth_resp = self.authorise()

        if auth_resp.status_code != 200:
            print("Error In getting the Bearer Token....")
            return
        
        self.access_token = auth_resp.json()['access_token']
        request_headers = {
            "Authorization": "Bearer {}".format(self.access_token)
        }

        twitter_data = pd.DataFrame(pd.read_csv("../Data Gathered/CollectedData.csv"))


        tweet_id = twitter_data['ID'].iloc[0]

        complete_url = self.base_url + str(tweet_id)


        resp = requests.get(complete_url, headers = request_headers)
        print(resp.json())


obj = MediaExtracter()
obj.mediaCollector()