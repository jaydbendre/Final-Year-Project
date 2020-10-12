import random
import numpy as np

data = list()
with open("cleanKeywords.txt", "r") as f:
    data = str(f.readlines()).split(",")
    random.shuffle(data)
    print(len(data))
    three_way_split = np.array_split(data, 2)

    for array, file_name in zip(three_way_split, ["Jay", "Vignesh"]):
        with open("{}.txt".format(file_name), "w") as x:
            for item in array:
                x.write("{},".format(item))
