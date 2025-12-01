#The IQR method:

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv("data.csv") #Reading the data frame fro a .csv file

#First, I use interpolate method to estimate numerical missing values, then I use dropna method to delete string missing values.
df_interp = df.interpolate(method = 'linear', limit_direction = 'forward') #The interpolate method
df_drop = df_interp.dropna(axis = 0, how = 'any') #The dropna method
df_new = df_drop #Therefore, our data frame from now on is "df_new".

q1 = df_new.quantile(0.25) #Calculating the quartiles
q3 = df_new.quantile(0.75)
iqr = q3 - q1

with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None): #Showing the outliers
    print((df_new <= (q1 - 1.5 * iqr)) | (df_new >= (q3 + 1.5 * iqr)))

# df_drop = df_interp.dropna([]) #Dropping the row containing outlier


