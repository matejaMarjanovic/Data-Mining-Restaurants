import pandas as pd
print("***********", "*zomatoCountryAdded.csv*", "***********", "\n", sep="\n")

df_restaurants = pd.read_csv("../data/zomatoMissingValuesRemoved.csv")
print(df_restaurants.head(), "\n")
print(df_restaurants.count(), "\n")
print(df_restaurants.describe(), "\n")
for column in df_restaurants.columns:
    print("Count values in column " + column, "\n")
    print(df_restaurants[column].value_counts(dropna=False))
