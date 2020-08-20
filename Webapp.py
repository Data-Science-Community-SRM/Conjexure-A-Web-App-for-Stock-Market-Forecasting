import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import json
import pymongo
import datetime
import pandas_datareader as web


user = "Abhishek"
password = "681dmxUsOW4DZWlr"

client = pymongo.MongoClient(f"mongodb+srv://{user}:{password}@clust01.7nxse.mongodb.net")

db = client.predictions

@st.cache(persist=True, max_entries = 5)
def getpred(start,end):
    pred = db.data.find_one({'date':{'$lt': end, '$gte': start}})
    print("Got OutPut") 
    if pred is None:
        st.title("Sorry we aren't availible")
        return None
    return pred

today = datetime.datetime.today()
start = datetime.datetime(today.year,today.month,today.day,0,0)
end = datetime.datetime(today.year,today.month,today.day,23,59)
pred = getpred(start,end)
if pred == None:
    exit()

st.image('image.jpeg',use_column_width=True)
st.title("Conjexure ~ Stock Price Forecasting 📈")
st.header("Welcome to  Conjexure!")
st.markdown("""
In this Machine Learning application, we have used the historical stock price data for Alphabet (GOOGL) and Apple Inc. (AAPL) to forecast their price in a specified future window
""")
st.markdown("""
"We have used the Tensorflow and Keras APIs to build a stacked LSTM model with a convolutional as well as a lambda layer. We trained our model on a roughly four-month period from March 1st, 2020 through July 20th, 2020.
""")

info = json.loads(open("info.json","r").read())

CH1 = st.selectbox("Stock", info["Stocks"])

week = ["7","14","21"]
CH2 = st.selectbox("Choice of Future Forecast Period", week)

#S_data = pd.read_csv("HistData/data_"+CH1+".csv")

@st.cache(persist=True, max_entries = 2)
def getstock(CH1):
    S_data = web.DataReader(CH1,data_source='yahoo',start = "2020-01-04")
    return S_data

S_data = getstock(CH1)

#S_data["Date"] = pd.to_datetime(S_data["Date"])

P_data = pd.DataFrame({'A':pred[CH1][CH2][0]})
P_data.index = pd.date_range(start = today, periods = int(CH2))

#S_data = S_data.set_index("Date")

forplot = S_data.Close.max() + S_data.Close.mean()/4

with st.spinner('Wait for it...'):
    plt.figure(figsize=(10,5))
    plt.grid()
    plt.ylim(0,forplot)
    plt.plot(S_data["Close"],label = "Market Value")
    plt.plot(P_data, label = "Prediction")
    plt.legend()
    st.pyplot()

