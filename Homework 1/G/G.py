#The Z-score method:

import pandas as pd
from matplotlib import pyplot
import numpy as np

df = pd.read_csv("data.csv") #Reading the data frame fro a .csv file

#First, I use interpolate method to estimate numerical missing values, then I use dropna method to delete string missing values.
df_interp = df.interpolate(method = 'linear', limit_direction = 'forward') #The interpolate method
df_drop = df_interp.dropna(axis = 0, how = 'any') #The dropna method
df_new = df_drop #Therefore, our data frame from now on is "df_new".
# df_new_column = df_new['infected_by']
# df_new_column = df_new['birth_year']
df_new_column = df_new['id']

#Method 1: Using scatterplot to detect outliers:
pyplot.figure() #Scatter Plotiing
pyplot.scatter(df_new['state'], df_new['birth_year'])
pyplot.show()

#Method 2: Using Z-score to detect outliers:
outliers = []

def detect_outlier(data):

    threshold = 3
    mean_data = np.mean(data)
    std_data = np.std(data)

    for item in data:
        z_score = (item - mean_data) / std_data
        if np.abs(z_score) > threshold:
            outliers.append(item)
    return outliers

outlier_df = detect_outlier(df_new_column)
print(outlier_df)

df_filtered = df_new.drop([162])
with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None):
    print(df_filtered)

