import json
import pandas_datareader as web
import pandas as pd
import datetime
import pymongo



#info = json.loads(open("info.json","r").read())

def updatedata(stocks):
    for i in stocks:
        df=web.DataReader(i,data_source='yahoo')
        df.to_csv("stockdata/data_"+i+".csv")

#updatedata(info["Stocks"])


user = "Abhishek"
password = "681dmxUsOW4DZWlr"


client = pymongo.MongoClient(f"mongodb+srv://{user}:{password}@clust01.7nxse.mongodb.net")

db = client.predictions

today = datetime.datetime.today()
start = datetime.datetime(today.year,today.month,3,0,0)
end = datetime.datetime(today.year,today.month,3,23,59)
print(start,end,datetime.datetime.now())
#db.acess.insert_one({"date":datetime.datetime.now()})

print(db.acess.find_one({'date':{'$lt': end, '$gte': start}}))

print("done now")

post = {
            "date":datetime.datetime.now()
            "stockname" : {
                "7":[],
                "14":[],
                "21":[],
            }
        }



if __name__ == "__main__":
    if EntryExists() == False:
        A = AllModelsDontExist()
        if A is not None:
            MakeTrainSave(A)
        dat = MakePreds()
        post = MakeReq(dat)
        db.data.insert_one{post}
        
        
         



    