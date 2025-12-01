import pandas as pd

df = pd.read_csv("data.csv") #Reading the data frame fro a .csv file

with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None):
    print(pd.isna(df))

# Filling missing values:
# Method 1: 
with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None):
    print(df.fillna(0))

# Method 2:
with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None):
    print(df.fillna(method = 'pad'))

# Method 3:
with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None): #Thus, if there is missing value at the end of the dataset, it will propogate to the upper layers; thus, the missing valuses increases, and this is not what we basicalluy want, and this is not the best method.
    print(df.fillna(method = 'bfill')) 

# Method 4:
with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None): #This is not a good method, too. Because we still don't have any value for the missing values.
    print(df['region'].fillna("No region", inplace = True)) 

# Method 5:
with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None):
    print(df.replace(to_replace = np.NaN, value = -99))

# Meyhod 6:
with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None):
    print(df.interpolate(method = 'linear', limit_direction = 'forward')) #This method only works for filling numerical missing values. Therefore, it should be used in combination with for example #Method 4 to cover the non-numerical missing values, as well.


# deleting missing values:
# Method 7: 
with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None):
    print(df.dropna())

# Method 8:
with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None): #This is not a good method since it still has rows with missing values. Actually, we may never have rows whose elements are all missing; therefore, these rows won't get deleted and missing values still exist in our data frame.
    print(df.dropna(how = 'all'))

# Method 9: 
with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None): #Droopping the columns that contain NaN
    print(df.dropna(axis = 1))

#Method 10: #***I think so far, this is the best method, which covers for both numerical and non-numerical missing values.
new_df = df.dropna(axis = 0, how = 'any')
with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None): #Droopping the rows that contain NaN
    print(new_df)
    
print("\nOld data frame length:", len(df)) 
print("New data frame length:", len(new_df))  
print("Number of rows with at least 1 NaN value: ", (len(df) - len(new_df)))


