import pandas as pd

df = pd.read_csv("../data/ComparedPriceAndAvgSalary.csv")

df = df.sort_values(by = "Votes")

votesData = []
for i, row in df.iterrows():
    if i < len(df.index)/3.0:
        votesData.append("Low")
    elif  i < len(df.index)*2/3.0:
        votesData.append("Medium")
    else:
        votesData.append("High")
        
df["# Votes"] = pd.Series(votesData, index = df.index)

with open("AddedCategoricalVotes.csv", "w") as csvFile:
    csv = df.to_csv()
    csvFile.write(csv)
