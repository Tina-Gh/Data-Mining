import pandas as pd

df = pd.read_csv("data.csv") #Reading the data frame fro a .csv file

print("The size of the data is:")
print(df.size)

print("\nThe dimention of the table is:")
print(df.shape)

print ("\nThe names of the columns are:") #printing the names of the columns
for col in df.columns:
    print(col) 

