import pandas as pd

df = pd.read_csv("ComparedPriceAndAvgSalary.csv")

allCuisines = []
for i, row in df.iterrows():
    cuisines = row["Cuisines"]
    for cuisine in cuisines.replace(" ", "").split(","):
        if cuisine not in allCuisines:
            allCuisines.append(cuisine)
            
allCuisinesData = [[] for i in range(len(allCuisines))]

for i, row in df.iterrows():
    for k in range(len(allCuisines)):
        if allCuisines[k] in row["Cuisines"].replace(" ", "").split(","):
            allCuisinesData[k].append(1)
        else:
            allCuisinesData[k].append(0)
            
for cuisineData in allCuisinesData:
    df[allCuisinesData.index(cuisineData)] = pd.Series(cuisineData, index = df.index)
    
with open("AddedCuisineCols.csv", "w") as csvFile:
    csv = df.to_csv()
    csvFile.write(csv)
