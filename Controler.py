import json
import pandas_datareader as web
import pandas as pd
import datetime
import pymongo

from pathlib import Path
import StockModel

print("Finished ")

info = json.loads(open("info.json","r").read())


idkwhy = [(i,j) for i in info["Stocks"] for j in ["7","14","21"]]
#updatedata(info["Stocks"])

user = "Abhishek"
password = "681dmxUsOW4DZWlr"


client = pymongo.MongoClient(f"mongodb+srv://{user}:{password}@clust01.7nxse.mongodb.net")

db = client.predictions

post = {
            "date":datetime.datetime.now(),
            "stockname": {
                "7":[],
                "14":[],
                "21":[],
            }
        }

def updatedata():
    for i in info["Stocks"]:
        df=web.DataReader(i,data_source='yahoo')
        df.to_csv("HistData/data_"+i+".csv")

def EntryExists():
    today = datetime.datetime.today()
    # change 3 later
    start = datetime.datetime(today.year,today.month,3,0,0)
    end = datetime.datetime(today.year,today.month,3,23,59)
    return db.acess.find_one({'date':{'$lt': end, '$gte': start}}) == False

def ModelPath(A,B):
    return "Models/" + A  + "_" + B  +".h5"

def AllModelsDontExist():
    A = []
    for i,j in idkwhy:
        C = ModelPath(i,j)
        if Path(C).exists() == False:
            A.append([i,j])
    return A

def MakeTrainSave(L):
    for i in L:
        S, days = i
        S_data = pd.read_csv("HistData/data_"+S+".csv")
        Mod = StockModel.Model_related_things(int(days))
        Mod.NewModel()
        S_data_close = S_data.Close.values
        Mod.TrainModel(S_data_close,2)
        Mod.SaveModel(ModelPath(S,days))

def MakePreds():
    for i,j in idkwhy:
        print(i,j)

    



if __name__ == "__main__":
    if EntryExists() == False:
        #updatedata()
        print("works")
        A = AllModelsDontExist()
        print(A)
        if len(A)!= 0:
            MakeTrainSave(A)
        dat = MakePreds()
        post = MakeReq(dat)
        db.data.insert_one(post)
        
        
         



    