import pandas as pd
from geopy.geocoders import Nominatim
import numpy as np

df = pd.DataFrame(
    pd.read_csv(
        "geopy_tester.csv"
    )
)

geolocator = Nominatim(user_agent="soulage")


def update_coords_lat(item):
    print(item)
    if item == "":
        return np.NaN
    else:
        location = geolocator.geocode(item)
        if location == None:
            return np.NaN

        return location.latitude


def update_coords_long(item):
    if item == "":
        return np.NaN
    else:
        location = geolocator.geocode(item)
        if location == None:
            return 0.0

        return location.longitude


def accuracy_calculator_lat(item):
    total = item["p_coord_lat"]
    difference = abs(item["l_coord_lat"] - item["p_coord_lat"])
    return 100.0-abs((difference/total)*100)


def accuracy_calculator_long(item):
    total = item["p_coord_long"]
    difference = abs(item["l_coord_long"] - item["p_coord_long"])
    return 100.0-abs((difference/total)*100)


df["p_coord_lat"] = df["location"].apply(update_coords_lat, 1)
df["p_coord_long"] = df["location"].apply(update_coords_long, 1)
df["l_coord_lat"] = df["local_location"].apply(update_coords_lat, 1)
df["l_coord_long"] = df["local_location"].apply(update_coords_long, 1)
df["lat_accuracy"] = df.apply(accuracy_calculator_lat, 1)
df["long_accuracy"] = df.apply(accuracy_calculator_long, 1)

with open("geopy_tester.csv", "w", encoding="utf-8") as f:
    df.to_csv(f, index=False)
