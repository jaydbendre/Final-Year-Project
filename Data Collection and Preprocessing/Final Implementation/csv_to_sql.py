from pandas.io import sql
import MySQLdb
import pandas as pd
from sqlalchemy import create_engine


class CSV_SQL_Pipeline():
    """
    To dump csv to a sql table
    """

    def dumper(self):
        sqlEngine = create_engine(
            "mysql+pymysql://root:@127.0.0.1/reveliumdatawarehouse", pool_recycle=3600)
        con = sqlEngine.connect()

        df = pd.DataFrame(
            pd.read_csv(
                "CleanedCollectedData.csv", index_col="id"
            )
        )

        df.to_sql(con=con, name="data", if_exists="append")

        con.close()


CSV_SQL_Pipeline().dumper()
