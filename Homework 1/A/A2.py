#Method 1: Reading the csv file without Pandas

import csv

with open ("data.csv", newline = '') as csvfile:
    spamreader = csv.reader(csvfile, delimiter = ' ', quotechar = '|')
    for row in spamreader:
        print(' '.join(row))
