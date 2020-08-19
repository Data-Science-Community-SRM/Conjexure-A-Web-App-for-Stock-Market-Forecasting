import json
import pandas_datareader as web
import pandas as pd
import datetime
import pymongo

from pathlib import Path
import StockModel

print("Imported Modules")

info = json.loads(open("info.json","r").read())

idkwhy = [(i,j) for i in info["Stocks"] for j in ["7","14","21"]]

user = "Abhishek"
password = "681dmxUsOW4DZWlr"

client = pymongo.MongoClient(f"mongodb+srv://{user}:{password}@clust01.7nxse.mongodb.net")

db = client.predictions

post = {
            "date":datetime.datetime.now(),
        }

def updatedata():
    for i in info["Stocks"]:
        df=web.DataReader(i,data_source='yahoo',start = "2020-01-04")
        df.to_csv("HistData/data_"+i+".csv")

def EntryExists():
    today = datetime.datetime.today()
    # change 3 later
    start = datetime.datetime(today.year,today.month,today.day,0,0)
    end = datetime.datetime(today.year,today.month,today.day,23,59)
    return db.data.find_one({'date':{'$lt': end, '$gte': start}}) != None

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
        Mod.TrainModel(S_data_close,100)
        Mod.SaveModel(ModelPath(S,days))

def MakePreds():
    for S,days in idkwhy:
        Mod = StockModel.Model_related_things(int(days))
        S_data = pd.read_csv("HistData/data_"+S+".csv")
        S_data_close = S_data.Close.values
        Mod.loadmodel(ModelPath(S, days))
        if S not in post.keys():
            post[S] = {}
        post[S][days] = None
        post[S][days] = Mod.ServePred(S_data_close)        

def main():
    if EntryExists() == False:
        updatedata()
        print("Posting predictions")
        A = AllModelsDontExist()
        if len(A)!= 0:
            MakeTrainSave(A)
        MakePreds()
        db.data.insert_one(post)
        print(post)


if __name__ == "__main__":
    main()