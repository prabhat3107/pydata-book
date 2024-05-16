import random
import datetime

data_dict = {'Time':'', 'Feed':"PB-NAMR",'IDP_symbol':"",'Contrib_symbol':"",'BID':"",'ASK':"",'TRDPRC_1':"",'postID':""}
error_dict = {'Time':'','Error_Code':"",'Error_Text':"",'postID':""}
#generate test data
with open('TRCC_Data.csv', 'w') as csvfile, open('conduit_error.csv', 'w') as error_csvfile :
    postID = 1001
    FS='\x01'
    #FS=','
    #range(0,100000000) generates 17G file
    for i in range(0,10000000):
        x=str(random.randint(1,50))
        time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")
        data_dict['Time']=time_stamp
        data_dict["IDP_symbol"] = "SYM_"+ x +".contrib"
        data_dict["Contrib_symbol"] = "JPX_"+ x + ".JX"
        y=random.uniform(10.10,30.90)
        data_dict["ASK"]=str(y)
        data_dict["BID"]=str( y - 0.3)
        data_dict["TRDPRC_1"]=str(y - 0.3)
        data_dict["postID"]= postID + i
        error_dict['Time'] = time_stamp
        error_dict["Error_Code"] = "Rejected"
        error_dict["Error_Text"] = "Invalid Symbol"
        error_dict["postID"] = postID + i
        trcc_line=""
        for key,value in data_dict.items():
            trcc_line=trcc_line + f"{key}={value}{FS}"
        trcc_line=trcc_line.rstrip(FS)
        csvfile.write(f"{trcc_line}\n")

        error_line = ""
        for key,value in error_dict.items():
            error_line=error_line + f"{key}={value}{FS}"
        error_line=error_line.rstrip(FS)
        error_csvfile.write(f"{error_line}\n")

#generate test error logs
