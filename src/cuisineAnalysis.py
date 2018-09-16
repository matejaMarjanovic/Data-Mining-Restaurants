import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ComparedPriceAndAvgSalary.csv")

allCuisines = {}
for i, row in df.iterrows():
    cuisines = row["Cuisines"]
    for cuisine in cuisines.replace(" ", "").split(","):
        if cuisine not in allCuisines:
            allCuisines[cuisine] = 1
        else:
            allCuisines[cuisine] += 1

forDeletion = []
others = 0
for k, v in allCuisines.items():
    if v <= 25:
        forDeletion.append(k)
        others += v

for e in forDeletion:
    del allCuisines[e]

allCuisines["Others"] = others

x = range(len(list(allCuisines.keys())))
plt.xticks(x,  list(allCuisines.keys()))
locs, labels = plt.xticks()
plt.setp(labels, rotation=80)
plt.bar(x, list(allCuisines.values()))
plt.show()
plt.close()
