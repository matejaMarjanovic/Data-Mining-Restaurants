import pandas as pd
import matplotlib.pyplot as plt
import statistics as stat

dfRest = pd.read_csv("ComparedPriceAndAvgSalary.csv")

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

plt.bar(range(len(countries)), averagePrice, tick_label = countries, color = "red")
plt.show()

plt.bar(range(len(countries)), meanPercent, tick_label = countries, color = "green")
plt.show()

plt.bar(range(len(countries)), medianPercent, tick_label = countries, color = "orange")
plt.show()
