import requests
import json
import base64
import pandas as pd
import numpy as np
import time


class MediaDownloadTwitter():
    # def __init__(self, starting_index, batch_size=100):
    #     self.error_codes = [400, 401, 403, 404, 429, 444, 499]
    #     self.starting_index = starting_index
    #     self.batch_size = batch_size

    def authorise(self):
        creds = dict()
        with open("../TwitterCred.json", "r") as f:
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

    def download_media(self, id):
        auth_resp = self.authorise()

        if auth_resp.status_code == 200:
            access_token = auth_resp.json()["access_token"]

            search_headers = {
                "Authorization": "Bearer {}".format(access_token)
            }

            search_url = "https://api.twitter.com/2/tweets/{}?expansions=attachments.poll_ids,attachments.media_keys,author_id,entities.mentions.username,geo.place_id,in_reply_to_user_id,referenced_tweets.id,referenced_tweets.id.author_id&media.fields=duration_ms,height,media_key,preview_image_url,type,url,width&tweet.fields=attachments,author_id,context_annotations,conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,possibly_sensitive,referenced_tweets,source,text,withheld".format(
                id)

            # search_params = {
            #     "id": "1297760253640146944"
            # }

            search_resp = requests.get(
                search_url, headers=search_headers)

            data = search_resp.json()

            for k, v in data.items():
                print(k, "\t", v)


MediaDownloadTwitter().download_media(1297512878203973637)
