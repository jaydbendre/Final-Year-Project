import requests
import json
import base64
import pandas as pd
import time
import numpy as np
from geopy.geocoders import Nominatim


class LocationUsingAPI():
    """
    Used to obtain location from a tweet
    """

    def __init__(self, starting_index, batch_size=100):
        self.error_codes = [400, 401, 403, 404, 429, 444, 499]
        self.starting_index = starting_index
        self.batch_size = batch_size

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
            twitter_id = twitter_data["ID"][self.starting_index:
                                            self.starting_index+self.batch_size]
            with open("last_position_updated.txt", "w") as f:
                f.write(str(self.starting_index+self.batch_size))
            i = 0
            geo_data_dictionary = dict()
            for t_id in twitter_id:
                print("Tweet {} analyzed".format(i+1))
                i += 1
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
                elif len(status_code) == self.batch_size:
                    break
                else:
                    tweet_data = search_resp.json()
                    geo_data_dictionary[tweet_data["id"]] = tweet_data

            with open("geoData.json", "w") as f:
                json.dump(geo_data_dictionary, f)

            return geo_data_dictionary
        else:
            return {"Error": "No data found , {} error".format(auth_resp.status_code)}

    def populate_csv(self, data_dictionary):
        geolocator = Nominatim(user_agent="soulage")
        print(data_dictionary.keys())

        def handle_record(item):

            if data_dictionary[item]["geo"] == None and data_dictionary[item]["place"] == None and data_dictionary[item]["coordinates"] == None:
                user_location = data_dictionary[item]["user"]["location"]
                if user_location == "":
                    return np.NaN
                else:
                    return user_location
            else:
                place = data_dictionary[item]["place"]["full_name"]
                return place

        def update_coords(item):
            if item == "":
                return np.NaN
            else:
                location = geolocator.geocode(item)
                if location == None:
                    return np.NaN
                return (location.latitude, location.longitude)

        twitter_data = pd.DataFrame(
            pd.read_csv("CollectedData.csv")
        )

        twitter_data = twitter_data[self.starting_index:
                                    self.starting_index+self.batch_size - 1]
        twitter_data["location"] = twitter_data["ID"].apply(handle_record, 1)

        twitter_data["coordinates"] = twitter_data["location"].apply(
            update_coords, 1)
        with open("updatedCollectedData.csv", "w", encoding="utf-8") as f:
            twitter_data.to_csv(f, index=False, encoding="utf-8")
        pass


starting_index = 0
with open("last_position_updated.txt", "r") as f:
    starting_index = int(f.read())

obj = LocationUsingAPI(starting_index, 20)

data_dictionary = obj.extract_location()
obj.populate_csv(data_dictionary)
