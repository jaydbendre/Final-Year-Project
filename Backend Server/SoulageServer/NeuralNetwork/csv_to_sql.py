from pandas.io import sql
import MySQLdb
import pandas as pd
from sqlalchemy import create_engine
from sentiment_model import SentimentAnalyzer
from apps import NeuralnetworkConfig
from tensorflow.keras.preprocessing import image
import requests
from io import BytesIO
import numpy as np
import glob
from DataCollection.data_collection_and_preprocessing_helper import DataCollectionAndPreprocessing as DP
import json
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

classes = {'Explicit': 0,
           'Meme': 1,
           'Nature': 2,
           'Other': 3,
           'Poster': 4,
           'Potrait': 5,
           'Protests': 6,
           'cyclone': 7,
           'earthquake': 8,
           'flood': 9,
           'wildfire': 10}

sentiment_df = pd.DataFrame()
image_prediction_df = pd.DataFrame()
lda_df = pd.DataFrame()


class CSV_SQL_Pipeline():
    """
    To dump csv to a sql table
    """

    def __init__(self):
        self.sqlEngine = create_engine(
            "mysql+pymysql://root:@127.0.0.1/relevium", pool_recycle=3600)
        self.con = self.sqlEngine.connect()
        self.df = pd.DataFrame(
            pd.read_csv(
                "LDA Model/CleanedCollectedData.csv"
            )
        )

        # self.lda = pickle.load(open("LDA Model/lda_model.pk", "rb"))
        # self.count_vectorizer = pickle.load(
        #     open("LDA Model/count_vectorizer.pk", "rb"))
        with open("LDA Model/count_vectorizer.pk", "rb") as f:
            unpickler = pickle.Unpickler(f)
            self.count_vectorizer = unpickler.load()

        with open("LDA Model/lda_model.pk", "rb") as f:
            unpickler = pickle.Unpickler(f)
            self.lda = unpickler.load()

        self.df = self.df[:100]

    def dumper(self):
        self.df.to_sql(con=self.con, name="soulage_data_collection",
                       if_exists="append")

    def lda_dumper(self, item):
        global lda_df

        with open("file-test.txt", "w", encoding="utf-8") as f:
            f.write(item.text)

        tweet = open("file-test.txt", "r", encoding="utf-8")

        vectorized_tweet = self.count_vectorizer.transform(tweet)

        prediction = self.lda.transform(vectorized_tweet).tolist()[0]
        # prediction = np.round(prediction * 100, decimals=2)
        topic_idx = prediction.index(max(prediction))

        lda_pred = {
            "topic_id_id": topic_idx,
            "tweet_id_id": item.id
        }

        lda_pred_df = pd.DataFrame([lda_pred])
        lda_df = lda_df.append(lda_pred_df, ignore_index=True)
        pass

    def connection_terminate(self):
        self.con.close()

    def sentiment_analyze(self, item):
        global sentiment_df
        # print(item)
        text = item.text
        sa_obj = SentimentAnalyzer(text)
        text = sa_obj.text
        predictions = NeuralnetworkConfig.sentiment_predictor.predict(text)
        sent = np.round(np.dot(predictions, 100).tolist(), 0)[0]
        result = dict()

        for sentiment, value in zip(sa_obj.sent_to_id.keys(), sent):
            result[sentiment] = value
        result["tweet_id_id"] = item.id
        result_df = pd.DataFrame([result])
        sentiment_df = sentiment_df.append(result_df, ignore_index=True)

    def image_analyze(self, item):
        global image_prediction_df

        # print(item.id)
        if len(glob.glob("media/{}.*".format(item.id))) == 0:
            return False
        else:
            img = ""
            try:
                img = image.load_img(glob.glob("media/{}.*".format(item.id))[0],
                                     target_size=(128, 128), color_mode="rgb")
            except FileNotFoundError as e:
                return False
            img = image.img_to_array(img)
            img = np.expand_dims(img, axis=0)
            results = NeuralnetworkConfig.image_class_predictor.predict(img)
            i = 0
            image_data = dict()
            for keys in classes.keys():
                image_data[keys] = int(
                    float("{:.2f}".format(float(results[0][i] * 100))))
                i += 1

            # print(image_data.items())
            image_data["tweet_id_id"] = item.id
            image_df = pd.DataFrame([image_data])
            image_prediction_df = image_prediction_df.append(
                image_df, ignore_index=True)

    def topic_populator(self):
        topic_dict = dict()
        with open("LDA Model/topic_relevancy.json", "r") as f:
            topic_dict = json.load(f)

        data = list()
        for k, v in topic_dict.items():
            data.append(
                {
                    "id": k,
                    "topic_name": "Topic #{}".format(k),
                    "keywords": v["keywords"],
                    "ignore_flag": v["Ignore_or_not"]
                }
            )

        topic_df = pd.DataFrame(data)
        topic_df = topic_df.set_index("id")
        topic_df.to_sql(con=self.con, name="soulage_topics",
                        if_exists="append")

    def run(self):
        global sentiment_df
        global image_prediction_df
        global lda_df

        # self.topic_populator()

        # print(glob.glob("media/{}.*".format(1337735252349861888)))
        # return False
        # self.dumper()
        # self.df[["id", "text"]].apply(self.sentiment_analyze, 1)
        self.df[["id", "text"]].apply(self.lda_dumper, 1)
        # DP().mediaDownload(self.df)

        # self.df.apply(self.image_analyze, 1)
        # sentiment_df = sentiment_df.set_index("tweet_id_id")
        lda_df = lda_df.set_index("tweet_id_id")
        # sentiment_df.to_sql(con=self.con, name="soulage_tweet_sentiment",
        #                     if_exists="append")
        lda_df.to_sql(con=self.con, name="soulage_topic_tweet_map",
                      if_exists="append")

        # if image_prediction_df.empty:
        #     print("Empty")
        # else:

        #     image_prediction_df = image_prediction_df.set_index("tweet_id_id")

        #     image_prediction_df.to_sql(
        #         con=self.con, name="soulage_tweet_image_class", if_exists="append")

        # self.connection_terminate()
        pass


    # files = item
    # folder = "uploaded_files/"
    # fs = FileSystemStorage(location=folder)
    # filename = fs.save(files.name, files)
    # # with open("uploaded_files/test_file.jpg", "wb") as f:
    # #     f.write(files)
    # # print("Hello")
    # data = list()
    # img = image.load_img("uploaded_files/{}".format(files.name),
    #                      target_size=(128, 128), color_mode="rgb")
    # img = image.img_to_array(img)
    # img = np.expand_dims(img, axis=0)
    # results = NeuralnetworkConfig.image_class_predictor.predict(img)
    # i = 0
    # for keys in classes.keys():
    #     data.append(
    #         {
    #             "label": keys,
    #             "value": int(float("{:.2f}".format(float(results[0][i] * 100))))
    #         })
    #     i += 1
    # data_dict = {
    #     "data": data,
    #     "file_name": files.name
    # }
    # print("Hello")
    # return JsonResponse(data_dict, safe=False)
    # pass
CSV_SQL_Pipeline().run()
