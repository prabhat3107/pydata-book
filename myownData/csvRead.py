import time
import csv
import pandas as pd

dataDictionary = []
d1={}
t1=time.perf_counter(), time.process_time()
#with open('TRCC_Data.csv') as csvfile:
with open('conduit_error.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter='\x01')
    for row in reader:
        d1={}
        for i in range(0,len(row)):
            key,value = row[i].split('=')
            d1[key]=value
        dataDictionary.append(d1)
t2=time.perf_counter(), time.process_time()
print(f'Time taken to process the file :')
print(f'Real Time : {t2[0]-t1[0]}')
print(f'Processed Time : {t2[1]-t1[1]}')


t3=time.perf_counter(), time.process_time()
df = pd.DataFrame(dataDictionary)
t4=time.perf_counter(), time.process_time()
print(f'Time taken build a dataframe :')
print(f'Real Time : {t4[0]-t3[0]}')
print(f'Processed Time : {t4[1]-t3[1]}')
del dataDictionary
#write the datafame to CSV
#fileName='TRCC_pub_logs.csv'
fileName='conduit_error_logs.csv'

df.to_csv(fileName,index=False)

