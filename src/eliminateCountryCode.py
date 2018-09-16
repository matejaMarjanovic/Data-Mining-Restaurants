import xlrd
import pandas as pd

dfRestaurants = pd.read_csv("zomato.csv", encoding = "ISO-8859-1")
dfCountries = pd.read_excel('Country-Code.xlsx', sheetname="Sheet1", index_col = "Country Code")

countriesData = []
for i, row in dfRestaurants.iterrows():
    countryCode = int(row["Country Code"])
    countriesData.append(dfCountries.ix[countryCode]["Country"])

dfRestaurants["Country"] = pd.Series(countriesData, index = dfRestaurants.index)
dfRestaurants = dfRestaurants.drop(["Country Code"], axis = 1)

with open("zomatoCountryAdded.csv", "w") as csvFile:
    csv = dfRestaurants.to_csv(index = True)
    csvFile.write(csv)
