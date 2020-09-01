import wget
import pandas as pd
import os
import time
df = pd.DataFrame(
    pd.read_csv(
        "../Data Gathered/CollectedData.csv"
    )
)


def media_download(item):
    import requests
    import time

    url = item["medias"][2:-2]
    r = requests.get(
        url, stream=True)
    # converts response headers mime type to an extension (may not work with everything)
    ext = r.headers['content-type'].split('/')[-1]
    ext = ext.split(";")[0]
    # open the file to write as binary - replace 'wb' with 'w' for text files
    # search_term = item["search_term"].strip()
    search_term = item["search_term"]
    print(search_term)
    time.sleep(1)
    if os.path.isdir("../Data Gathered/Data/{}/media/".format(search_term)) == False:
        os.mkdir(
            "../Data Gathered/Data/{}/media/".format(search_term))
    with open("../Data Gathered/Data/{}/media/{}.{}".format(search_term, str(item["ID"]), ext), 'wb') as f:
        # iterate on stream using 1KB packets
        for chunk in r.iter_content(1024):
            f.write(chunk)  # write the file


media_df = df[df["has_media"] == True]
media_df = media_df[["ID", "search_term", "medias"]]

media_df = media_df.apply(media_download, 1)
