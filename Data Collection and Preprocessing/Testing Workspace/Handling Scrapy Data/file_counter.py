import glob

count_of_folders = glob.glob("../Data Gathered/Data/*")
print("Number of folders : ", len(count_of_folders))

total = 0
for folder in count_of_folders:
    count_of_files = glob.glob(folder+"/tweets/*")
    total += len(count_of_files)
    # print("Number of elements in {} : {}".format(folder, len(count_of_files)))

print("Total tweets collected : ", total)
