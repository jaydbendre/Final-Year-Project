# import glob

# read_files = glob.glob("*.txt")

# with open("result.txt", "wb") as outfile:
#     for f in read_files:
#         with open(f, "rb") as infile:
#             outfile.write(infile.read())

import re

data = []
with open("result.txt", "r") as file:
    data = file.readlines()
    print(data[0])
    data = list(set(data[0].split(",")))
    print(data[0])
    data = [re.sub(r"[^a-zA-Z0-9]+", ' ', k) for k in data]
    data.sort()

    data = data[1:]
    print(data)
    print(len(data))

with open("cleanKeywords.txt", "w") as file:
    for d in data:
        d = d.strip()
        file.write(d+",")
