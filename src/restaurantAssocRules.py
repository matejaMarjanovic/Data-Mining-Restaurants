import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

df = pd.read_csv("../data/restaurantsConvertedToEuro.csv")

allCuisines = []
for i, row in df.iterrows():
    cuisines = row["Cuisines"].replace(" ", "").split(",")
    for cuisine in cuisines:
        cuisine = cuisine
        if cuisine not in allCuisines:
            allCuisines.append(cuisine)

allCuisinesData = []
for i in range(len(allCuisines)):
    allCuisinesData.append([])

for i, row in df.iterrows():
    cuisines = row["Cuisines"].replace(" ", "").split(",")
    for ind in range(len(allCuisines)):
        if allCuisines[ind] in cuisines:
            allCuisinesData[ind].append(1)
        else:
            allCuisinesData[ind].append(0)

df2 = pd.DataFrame()
for ind in range(len(allCuisines)):
    df2[allCuisines[ind]] = pd.Series(allCuisinesData[ind], index = df.index)

allRatingTexts = ["Average", "Not rated", "Good", "Very Good", "Excellent", "Poor"]
ratingsData = [[] for i in range(len(allRatingTexts))]

for i, row in df.iterrows():
    for rating in allRatingTexts:
        if rating == row["Rating text"]:
            ratingsData[allRatingTexts.index(rating)].append(1)
        else:
            ratingsData[allRatingTexts.index(rating)].append(0)

for i in range(len(ratingsData)):
    df2[allRatingTexts[i]] = pd.Series(ratingsData[i], index = df2.index)

frequent_itemsets = apriori(df2, min_support=0.02, use_colnames=True)
print(frequent_itemsets)
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.3)
print(rules)
