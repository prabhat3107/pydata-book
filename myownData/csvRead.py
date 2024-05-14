import csv
import pandas as pd

dataDictionary = []
d1={}
with open('TRCC_Data.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        d1={}
        for i in range(0,len(row)):
            key,value = row[i].split('=')
            d1[key]=value
        dataDictionary.append(d1)

print(dataDictionary)

df = pd.DataFrame(dataDictionary)
print(df)