import pandas as pd
from matplotlib import pyplot

df = pd.read_csv("data.csv") #Reading the data frame fro a .csv file

#First, I use interpolate method to estimate numerical missing values, then I use dropna method to delete string missing values.
df_interp = df.interpolate(method = 'linear', limit_direction = 'forward') #The interpolate method
df_drop = df_interp.dropna(axis = 0, how = 'any') #The dropna method
df_new = df_drop #Therefore, our data frame from now on is "df_new".

pyplot.figure(); #Histogram Plotiing
pyplot.hist(df_new['birth_year']) 
pyplot.show()
pyplot.savefig('histogram.png')

pyplot.figure(); #Boxplot Plotiing
pyplot.boxplot(df_new['birth_year'])
pyplot.show()
pyplot.savefig('boxplot.png')

pyplot.figure(); #Scatter Plotiing
pyplot.scatter(df_new['state'], df_new['birth_year'])
pyplot.show()
pyplot.savefig('scatter.png')



