import glob

count_of_folders = glob.glob("Data/*")
print("Number of folders : ", len(count_of_folders))

for folder in count_of_folders:
    count_of_files = glob.glob(folder+"/tweets/*")
    print("Number of elements in {} : {}".format(folder, len(count_of_files)))
