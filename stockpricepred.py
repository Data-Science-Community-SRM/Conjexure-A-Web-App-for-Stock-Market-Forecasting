import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf

image_path = '/Users/adityashukla/Desktop/Programming/Python/business-1730089.jpeg'

st.image(image_path, use_column_width=True)

st.title("Conjexure ~ Stock Price Forecasting 📈")
st.markdown("In this Machine Learning application, we have used the historical stock price data for Alphabet (GOOGL) and Apple Inc. (APPL) to forecast its price in a specified future window.")
st.markdown("We have used Tensorflow and Keras to build an LSTM model in addition to a convolutional as well as a lambda layer. We trained our model on a four-month period from April 1st, 2020 through July 1st, 2020.")

path = ('/Users/adityashukla/Desktop/Programming/stock-market-or-sales-forecasting-using-lstm-with-rnn-master/DATA.csv')

@st.cache(persist=True)
def predict(forecast_window):
	model = load_model('stockpricepred.h5')
	model.predict()

def load_data(nrows):
	data = pd.read_csv(path, nrows = nrows)
	return data

data = load_data(125)
st.markdown("You may go over the raw data. We have used the closing price as the generic price.")
if st.checkbox("Show Raw Data"):
	st.write(data)

# Dropdown Menu to Choose Company Stock
st.subheader("Choose from Apple Inc. (APPL) and Alphabet Inc. (GOOGL) to predict their future stock prices.")
stock_choice = st.selectbox("Choice of Company Stock", ['Alphabet (GOOGL)','Apple (APPL)'])


st.subheader("Select the period (1-5 weeks) into the future for when you would like to see the forecast: ")
forecast_window = st.selectbox("Choice of Future Forecast Period", ['1 week','2 weeks','3 weeks','4 weeks','5 weeks'])

st.subheader("Graph of Stock Price Forecast for a period of %s after 1st July, 2020." % forecast_window)
# predict(forecast_window)