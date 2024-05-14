import random
import csv

data_dict = {'Feed':"PB-NAMR",'IDP_symbol':"",'Contrib_symbol':"",'BID':"",'ASK':"",'TRDPRC_1':"",'postID':""}

with open('TRCC_Data.csv', 'w') as csvfile:
    postID = 1001
    FS='\x01'
    for i in range(0,100000000):
        x=str(random.randint(1,50))
        data_dict["IDP_symbol"] = "SYM_"+ x +".contrib"
        data_dict["Contrib_symbol"] = "JPX_"+ x + ".JX"
        y=random.uniform(10.10,30.90)
        data_dict["ASK"]=str(y)
        data_dict["BID"]=str( y - 0.3)
        data_dict["TRDPRC_1"]=str(y - 0.3)
        data_dict["postID"]= postID + i
        line=""
        for key,value in data_dict.items():
            line=line + f"{key}={value}{FS}"
        line=line.rstrip('\x01')
        csvfile.write(f"{line}\n")


