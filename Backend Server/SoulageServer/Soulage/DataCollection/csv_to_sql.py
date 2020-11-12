from pandas.io import sql
import MySQLdb
import pandas as pd
from sqlalchemy import create_engine
# from ..apps import SoulageConfig
# from ..sentiment_model import SentimentAnalyzer


class CSV_SQL_Pipeline():
    """
    To dump csv to a sql table
    """

    def dumper(self):
        sqlEngine = create_engine(
            "mysql+pymysql://root:@127.0.0.1/relevium", pool_recycle=3600)
        con = sqlEngine.connect()

        df = pd.DataFrame(
            pd.read_csv(
                "CleanedCollectedData.csv", index_col="id"
            )
        )
        sentiment_df = pd.DataFrame()
        # sentiment_df[["sentiment", "tweet_id_id"]] = df[[
        #     "id", "text"]].apply(self.sentiment_predictor, 1)
        df.to_sql(con=con, name="soulage_data_collection", if_exists="append")
        # sentiment_df.to_sql(
        #     con=con, name="soulage_tweet_sentiment", if_exists="append")

        con.close()

    # def sentiment_predictor(self, id, text):
    #     sa_obj = SentimentAnalyzer(text)
    #     text = sa_obj.text
    #     predictions = SoulageConfig.predictor.predict(text)
    #     sent = np.round(np.dot(predictions, 100).tolist(), 0)[0]
    #     result = pd.DataFrame([sa_obj.sent_to_id.keys(), sent]).T
    #     result.columns = ["sentiment", "percentage"]
    #     result = result[result.percentage != 0]
    #     sentiment = result[result.percentage ==
    #                        result.percentage.max()].sentiment
    #     return [id, sentiment]
# CSV_SQL_Pipeline().dumper()
