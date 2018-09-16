import pandas as pd

df = pd.read_csv("zomatoMissingValuesRemoved.csv")

data = []
for i, row in df.iterrows():
    if row["Currency"] == "Botswana Pula(P)":
        data.append("Philippine peso(PHP)")
    else:
        data.append(row["Currency"])
        
df = df.drop(["Currency"], axis = 1)
df["Currency"] = pd.Series(data, index = df.index)

with open("BotswanaBugFixed.csv", "w") as csvFile:
    csv = df.to_csv(index = False)
    csvFile.write(csv)
