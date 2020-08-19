import requests
import json
import base64
import pandas as pd
import time


class LocationUsingAPI():
    """
    Used to obtain location from a tweet
    """

    def __init__(self):
        self.error_codes = [400, 401, 403, 404, 429, 444, 499]

    def authorise(self):
        creds = dict()
        with open("ourTwitterCred.json", "r") as f:
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

    def extract_location(self):
        auth_resp = self.authorise()

        if auth_resp.status_code == 200:
            access_token = auth_resp.json()["access_token"]
            print("Hi")
            search_headers = {
                "Authorization": "Bearer {}".format(access_token)
            }
            twitter_data = pd.DataFrame(
                pd.read_csv("CollectedData.csv")
            )

            status_code = list()
            twitter_id = twitter_data["ID"]
            geo_data_dictionary = dict()
            for t_id in twitter_id:
                search_url = "https://api.twitter.com/1.1/statuses/show.json"

                search_params = {
                    "id": str(t_id),
                }
                search_resp = requests.get(
                    search_url, headers=search_headers, params=search_params)

                status_code.append(search_resp.status_code)
                if search_resp.status_code != 200:
                    for x in status_code[-10:]:
                        if self.error_codes.count(x) > 5:
                            time.sleep(60)
                            break
                    continue
                else:
                    tweet_data = search_resp.json()
                    geo_data_dictionary[i] = tweet_data

            with open("geoData.json", "w") as f:
                json.dump(geo_data_dictionary, f)

            return geo_data_dictionary
        else:
            return {"Error": "No data found , {} error".format(auth_resp.status_code)}

    def populate_csv(self, data_dictionary):
        def handle_record(self, item):
            pass
        pass
