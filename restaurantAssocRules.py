import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

df = pd.read_csv("restaurantsConvertedToEuro.csv")

allCuisines = []
for i, row in df.iterrows():
    cuisines = row["Cuisines"].replace(" ", "").split(",")
    for cuisine in cuisines:
        cuisine = cuisine
        if cuisine not in allCuisines:
            allCuisines.append(cuisine)

#print(allCuisines)

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

#allCountries = []
#for i, row in df.iterrows():
    #country = row["Country"].strip()
    #if country not in allCountries:
        #allCountries.append(country)

#countriesData = [[] for i in range(len(allCountries))]

#for i, row in df.iterrows():
    #for country in allCountries:
        #if country == row["Country"]:
            #countriesData[allCountries.index(country)].append(1)
        #else:
            #countriesData[allCountries.index(country)].append(0)

#for i in range(len(countriesData)):
    #df2[allCountries[i]] = pd.Series(countriesData[i], index = df2.index)

    
#print (df2)

frequent_itemsets = apriori(df2, min_support=0.02, use_colnames=True)
print(frequent_itemsets)
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.3)
print(rules)
    
#with open("ColumnPerCuisine.csv", "w") as csvFile:
    #csv = df.to_csv(index = False)
    #csvFile.write(csv)
    
    
    
