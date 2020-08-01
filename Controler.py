import json
import pandas_datareader as web
import pandas as pd

info = json.loads(open("info.json","r").read())

def updatedata(stocks):
    for i in stocks:
        df=web.DataReader(i,data_source='yahoo')
        df.to_csv("data_"+i+".csv")

updatedata(info["Stocks"])        
    