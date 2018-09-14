import pandas as pd

dfSal = pd.read_csv("countrySalaries.csv")
dfRest = pd.read_csv("restaurantsConvertedToEuro.csv")

salariesDict = {}
for i, row in dfSal.iterrows():
    salariesDict[row["Country"]] = row["Average Salary"]
    
cmpData = []
for i, row in dfRest.iterrows():
    country = row["Country"]
    if row["Average Cost for two euro"] != 0:
        cmpData.append(row["Average Cost for two euro"]/salariesDict[country])
    else:
        cmpData.append(0)        
    
dfRest["Compared Price and Salary"] = pd.Series(cmpData, index = dfRest.index)

with open("ComparedPriceAndAvgSalary.csv", "w") as csvFile:
    csv = dfRest.to_csv(index = False)
    csvFile.write(csv)
