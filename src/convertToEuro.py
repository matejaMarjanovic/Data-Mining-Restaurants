import pandas as pd

dfRest = pd.read_csv("BotswanaBugFixed.csv")

currencyDict = {}
euroData = []
for i, row in dfRest.iterrows():
    currency = row["Currency"]
    if currency not in currencyDict:
        currencyDict[currency] = 1
        if currency == "Indian Rupees(Rs.)":
            currencyDict[currency] = 0.0119961216
        elif currency == "Dollar($)":
            currencyDict[currency] = 0.861109867
        elif currency == "Qatari Rial(QR)":
            currencyDict[currency] = 0.236503825
        elif currency == "Sri Lankan Rupee(LKR)":
            currencyDict[currency] = 0.00528979791
        elif currency == "Indonesian Rupiah(IDR)":
            currencyDict[currency] = 0.00005769436
        elif currency == "Philippine peso(PHP)":
            currencyDict[currency] = 0.0158873603
        elif currency == "Turkish Lira(TL)":
            currencyDict[currency] = 0.134882527
        elif currency == "NewZealand($)":
            currencyDict[currency] = 0.56440499
        elif currency == "Brazilian Real(R$)":
            currencyDict[currency] = 0.206911784
        elif currency == "Rand(R)":
            currencyDict[currency] = 0.0580379439
        elif currency == "Emirati Diram(AED)":
            currencyDict[currency] = 0.234432856
        else:
            currencyDict[currency] = 1.12327735

    print(row["Restaurant Name"])
    print(row["City"])
    print(row["Average Cost for two"])
    print("---------------------")
    euroData.append(currencyDict[currency]*float(row["Average Cost for two"]))
    
dfRest["Average Cost for two euro"] = pd.Series(euroData, index = dfRest.index)
    
with open("restaurantsConvertedToEuro.csv", "w") as csvFile:
    csv = dfRest.to_csv(index = False)
    csvFile.write(csv)
        
        
        
        
        
        
