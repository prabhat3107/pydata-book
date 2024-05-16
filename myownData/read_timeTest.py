import pandas as pd
import dask.dataframe as dd
import time
#FS = '\x01'
FS=','
trcc_publish_df = pd.read_csv('TRCC_pub_logs.csv',sep=FS)
error_df = pd.read_csv('conduit_error_logs.csv',sep=FS)

analysis_df = trcc_publish_df.merge(error_df[['Error_Code', 'Error_Text', 'postID']],how='left',on='postID')

print(trcc_publish_df.head())
print(error_df.head())
print(analysis_df.head().to_string())

#print(df.head())
#start = time.time()
#trcc_df = pd.read_csv('TRCC_Data.csv', sep=FS, header=None)
#end = time.time()
#print("Pandas: Read time:", end - start)
#print("#################")

#start = time.time()
#trcc_df = dd.read_csv('TRCC_Data.csv', sep=FS, header=None )
#important learning :
#Dask data frame search and replace is done using dd.replace function with regex as given below.
#d_df = d_df.replace("[postID=]",'', regex=True)
#error_df = dd.read_csv('conduit_error.csv', sep=FS, header=None )

#trcc_df.set_index('Date', inplace=True)
#analysis_df = dd.merge(trcc_df, error_df, how='left', left_on=7, right_on=3)

#print(analysis_df.head())


#print("Dask: Read time:", end - start)
#print("#################")



#trcc_df[7] = trcc_df[7].str.replace('postID=','')
#error_df = pd.read_csv('conduit_error.csv', sep=FS, header=None)
#error_df[3] = error_df[3].str.replace('postID=','')
#print(trcc_df.head().to_string())
#print(error_df.head().to_string())

#analysis_df = dd.merge(trcc_df, error_df[[1,2,3]], left_on=7, right_on=3)

#print(analysis_df.head().to_string())
