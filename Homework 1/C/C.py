import pandas as pd

df = pd.read_csv("data.csv") #Reading the data frame fro a .csv file

output = pd.DataFrame([df['birth_year'].max(), df['birth_year'].mean(), df['birth_year'].std()], ['max', 'mean', 'std']) # To show output in a table
print(output)

## To normally show the output:
# print("The max of the birth years is:")
# print(df['birth_year'].max())

# print("\nThe mean of the birth years is:")
# print(df['birth_year'].mean())

# print("\nThe std of the birth year is:")
# print(df['birth_year'].std())






