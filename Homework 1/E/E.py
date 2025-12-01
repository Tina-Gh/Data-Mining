import pandas as pd

df = pd.read_csv("data.csv") #Reading the data frame fro a .csv file
with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None):
    print(pd.isna(df))

print("\n")
#First, I use interpolate method to estimate numerical missing values, then I use dropna method to delete string missing values.
df_interp = df.interpolate(method = 'linear', limit_direction = 'forward') #The interpolate method

df_drop = df_interp.dropna(axis = 0, how = 'any') #The dropna method
with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None): #Droopping the rows that contain NaN
    print(df_drop)
    
print("\nOld data frame length:", len(df)) 
print("New data frame length:", len(df_drop))  
print("Number of rows with at least 1 NaN value: ", (len(df) - len(df_drop)))