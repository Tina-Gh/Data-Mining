#Method 2: Reading the csv file via Pandas

import pandas as pd

df = pd.read_csv("data.csv") #data frame #read the .csv file

with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', None): #method number 3 (please enlarge your command window to see the whole dataframe in allignment)
    print(df)

# rows = len(df) #method number 1 (But this method does not show the whole data frame, but only 5 rows by default.)
# print(df.head(rows))

# import csv #method number 3 (But this method is not beautifull, the more pretty one is methood number 3, bellow.)
# with open ("data.csv", newline = '') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter = ' ', quotechar = '|')
#     for row in spamreader:
#         print(' '.join(row))




