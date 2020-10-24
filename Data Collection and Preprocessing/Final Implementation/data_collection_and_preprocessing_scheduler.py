import data_collection_and_preprocessing_helper as d
import datetime as dt
import glob
data_collection_obj = d.DataCollectionAndPreprocessing()

i = 0
old_file_count = len(glob.glob("Data Gathered/*"))
while True:
    i += 1
    print("Collection round {} started at : {}".format(i, dt.datetime.now()))
    data_collection_obj.collectingDataUsingApi()
    print("Collection round {} finished at {}".format(i, dt.datetime.now()))
    files = glob.glob("Data Gathered/*")
    print("Number of new files collected after round {}: {}".format(
        i, len(files) - old_file_count))
    data_collection_obj.convert_folder_to_csv()
    print("File converted to CSV for round {}".format(i))
    data_collection_obj.clean_csv()
    print("CSV cleaned after round {}".format(i))
    old_file_count = len(files)
