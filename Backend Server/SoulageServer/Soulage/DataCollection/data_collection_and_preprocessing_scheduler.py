import data_collection_and_preprocessing_helper as d
import datetime as dt
import glob
import time
import csv_to_sql as cs

data_collection_obj = d.DataCollectionAndPreprocessing()
cs_ob = cs.CSV_SQL_Pipeline()

i = 0
old_file_count = len(glob.glob("Data Gathered/*"))
while True:
    i += 1
    collection_time = dt.datetime.now()
    print("Collection round {} started at : {}".format(i, dt.datetime.now()))
    time.sleep(1*30)
    end_time = dt.datetime.now()

    print("Collection round {} finished at {}".format(i, dt.datetime.now()))
    files = glob.glob("Data Gathered/*")

    print("Number of new files collected after round {}: {}".format(
        i, len(files) - old_file_count))
    data_collection_obj.convert_folder_to_csv(collection_time, end_time)
    print("File converted to CSV for round {}".format(i))
    data_collection_obj.clean_csv()

    print("CSV cleaned after round {}".format(i))
    old_file_count = len(files)

    cs_ob.dumper()
    print("Dump records in SQL")
