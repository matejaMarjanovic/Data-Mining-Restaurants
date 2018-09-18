import pandas as pd
import matplotlib.pyplot as plt
import statistics as stat

dfRest = pd.read_csv("../data/ComparedPriceAndAvgSalary.csv")

sumCountryPrices = {}
sumCountryPercentMean = {}
sumCountryPercentMedian = {}
for i, row in dfRest.iterrows():
    if row["Average Cost for two euro"] != 0:
        if row["Country"] not in sumCountryPrices:
            sumCountryPrices[row["Country"]] = []
            sumCountryPrices[row["Country"]].append(row["Average Cost for two euro"])
            
            sumCountryPercentMean[row["Country"]] = []
            sumCountryPercentMean[row["Country"]].append(row["Compared Price and Salary"])
            
        else:
            sumCountryPrices[row["Country"]].append(row["Average Cost for two euro"])
            sumCountryPercentMean[row["Country"]].append(row["Compared Price and Salary"])
        
for country, priceList in sumCountryPrices.items():
    sumCountryPrices[country] = sum(priceList)/len(priceList)
    sumCountryPercentMedian[country] = stat.median(sumCountryPercentMean[country])
    sumCountryPercentMean[country] = sum(sumCountryPercentMean[country])/len(sumCountryPercentMean[country])
    
countries = list(sumCountryPrices.keys())
averagePrice = list(sumCountryPrices.values())
meanPercent = list(sumCountryPercentMean.values())
medianPercent = list(sumCountryPercentMedian.values())


x = range(len(countries))
plt.xticks(x,  countries)
locs, labels = plt.xticks()
plt.setp(labels, rotation=80)
plt.bar(x, averagePrice)
plt.show()


x = range(len(countries))
plt.xticks(x,  countries)
locs, labels = plt.xticks()
plt.setp(labels, rotation=80)
plt.bar(x, meanPercent)
plt.show()

x = range(len(countries))
plt.xticks(x,  countries)
locs, labels = plt.xticks()
plt.setp(labels, rotation=80)
plt.bar(x, medianPercent)
plt.show()

plt.close()


