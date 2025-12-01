# I chose the 'region' column.

import pandas as pd

df = pd.read_csv("data.csv") #Reading the data frame fro a .csv file


print("The number of fields in the 'region' column is:")
print(df['region'].count())