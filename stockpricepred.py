import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
import tensorflow.keras.backend
import pandas_datareader as web
from sklearn.preprocessing import MinMaxScaler

# cover image used and streamlit function call to display image
image_path = ('/image.jpeg')
st.image(image_path, use_column_width=True)

# basic title and markdown
st.title("Conjexure ~ Stock Price Forecasting 📈")
st.header("Welcome to Conjexure!")
st.markdown("In this Machine Learning application, we have used the historical stock price data for Alphabet (GOOGL) and Apple Inc. (AAPL) to forecast their price in a specified future window.")
st.markdown("We have used the Tensorflow and Keras APIs to build a stacked LSTM model with a convolutional as well as a lambda layer. We trained our model on a roughly four-month period from March 1st, 2020 through July 20th, 2020.")

path_googl = ('/data_googl.csv')
path_aapl = ('/data_aapl.csv')

# function to load separate models on the basis of user choice
@st.cache(allow_output_mutation=True)
def load_model(forecast_window):
	if forecast_window == '1 week':
		model = keras.models.load_model('/model1.h5')
	elif forecast_window == '2 weeks':
		model = keras.models.load_model('/model2.h5')
	elif forecast_window == '3 weeks':
		model = keras.models.load_model('/model3.h5')
	elif forecast_window == '4 weeks':
		model = keras.models.load_model('/model4.h5')
	elif forecast_window == '5 weeks':
		model = keras.models.load_model('/model5.h5')

	# model._make_predict_function()
	model.summary()
	return model

# function to load data from dataset
@st.cache(persist=True)
def load_data(path, nrows):
	data = pd.read_csv(filepath_or_buffer = path, nrows = nrows)
	return data

# simple mapping function to map forecast input strings to relevant integers
def mapper(forecast_window):
	if forecast_window == '1 week':
		return 7
	elif forecast_window == '2 weeks':
		return 14
	elif forecast_window == '3 weeks':
		return 21
	elif forecast_window == '4 weeks':
		return 28
	elif forecast_window == '5 weeks':
		return 35

# windowing function
def windowed_dataset(series, window_size = 31,predday = 7, batch_size = 32, shuffle_buffer= 1000):
    ds = tf.data.Dataset.from_tensor_slices(series)
    ds = ds.window(window_size + predday, shift=1, drop_remainder=True)
    ds = ds.flat_map(lambda w: w.batch(window_size + predday))
    ds = ds.shuffle(shuffle_buffer)
    ds = ds.map(lambda w: (w[:-7], tf.squeeze(w[-7:])))
    return ds.batch(batch_size).prefetch(3)

# plotting function to plot the final forecast line graph
def plot_graph(forecast, forecast_window_int, a, b):
	if forecast_window_int == 7:
		plt.plot(np.arange(0,31), a[0])
		plt.plot(np.arange(31,38), forecast[0], "--")
		plt.plot(np.arange(31,38), b[0])
	elif forecast_window_int == 14:
		plt.plot(np.arange(0,63), a[0])
		plt.plot(np.arange(63,77), forecast[0], "--")
		plt.plot(np.arange(63,77), b[0])
	elif forecast_window_int == 21:
		plt.plot(np.arange(1,91), a[0])
		plt.plot(np.arange(91,112), forecast[0], "--")
		plt.plot(np.arange(91,112), b[0])		
	elif forecast_window_int == 28:
		plt.plot(np.arange(1,121), a[0])
		plt.plot(np.arange(121,149), forecast[0], "--")
		plt.plot(np.arange(121,149), b[0])
	elif forecast_window_int == 35:
		plt.plot(np.arange(1,151), a[0])
		plt.plot(np.arange(151,186), forecast[0], "--")
		plt.plot(np.arange(151,186), b[0])
	
	plt.legend(["Input of 30 days","Prediction","Truth Value"])
	st.pyplot()

# main function
if __name__ == "__main__":
	st.markdown("You may go over the raw data for Alphabet or Apple. Just go to the sidebar and select your stock of choice. We have used the closing price as the generic price. ")
	choice = st.selectbox("Show Raw Data", ['Alphabet (GOOGL)', 'Apple (APPL)'])
	if choice == 'Alphabet (GOOGL)':
		data = load_data(path_googl,100)
		st.write(data)
	elif choice == 'Apple (APPL)':
		data = load_data(path_aapl,100)
		st.write(data)

	# Dropdown Menu to Choose Company Stock
	st.subheader("Choose from Apple Inc. (AAPL) and Alphabet Inc. (GOOGL) to predict their future stock prices.")
	stock_choice = st.selectbox("Choice of Company Stock", ['Alphabet (GOOGL)','Apple (AAPL)'])

	#st.subheader("Select the period (1-5 weeks) into the future for when you would like to see the forecast: ")
	#forecast_window = st.selectbox("Choice of Future Forecast Period", ['1 week','2 weeks','3 weeks','4 weeks','5 weeks'])

	if stock_choice == 'Alphabet (GOOGL)':
		# Reading the data
		df_test = web.DataReader('GOOGL',data_source='yahoo',start='03-01-2020',end='07-20-2020')
		
		# Displaying historical data for Alphabet
		st.subheader("Graph of Alphabet Inc.'s Historical Stock Prices")
		st.line_chart(df_test['Close'])
		
		# Inputting forecast window
		st.subheader("Select the period (1-5 weeks) into the future for when you would like to see %s's forecast: " % stock_choice)
		forecast_window = st.selectbox("Choice of Future Forecast Period", ['1 week','2 weeks','3 weeks','4 weeks','5 weeks'])
		forecast_window_int = mapper(forecast_window)

		# Choosing the closing data and reshaping into input shape
		x_test = df_test['Close']
		x_test = np.array(x_test).reshape(-1,1)

		# Scaling and windowing the input
		scaler1 = MinMaxScaler(feature_range=(0,0.75))
		xt1 = scaler1.fit_transform(x_test)
		xt = windowed_dataset(xt1, predday=forecast_window_int)
		
		a, b = next(iter(xt))

		# load that model which is asked by the user and predict based on given timestep
		model = load_model(forecast_window)
		forecast = model.predict(a)
	elif stock_choice == 'Apple (AAPL)':
		# Reading the data
		df_test = web.DataReader('AAPL',data_source='yahoo',start='03-01-2020',end='07-20-2020')

		# Displaying historical data for Alphabet
		st.subheader("Graph of Apple Inc.'s Historical Stock Prices")
		st.line_chart(df_test['Close'])

		# Inputting forecast window
		st.subheader("Select the period (1-5 weeks) into the future for when you would like to see %s's forecast: " % stock_choice)
		forecast_window = st.selectbox("Choice of Future Forecast Period", ['1 week','2 weeks','3 weeks','4 weeks','5 weeks'])
		forecast_window_int = mapper(forecast_window)

		# Choosing the closing data and reshaping into input shape
		x_test = df_test['Close']
		x_test = np.array(x_test).reshape(-1,1)

		# Scaling and windowing the input
		scaler1 = MinMaxScaler(feature_range=(0,0.75))
		xt1 = scaler1.fit_transform(x_test)
		xt = windowed_dataset(xt1, predday=forecast_window_int)
		
		a, b = next(iter(xt))

		# load that model which is asked by the user and predict based on given timestep
		model = load_model(forecast_window)
		forecast = model.predict(a)

	# Plotting of future forecast graph
	st.subheader("Future forecast for %s for a period of %s after 20th July, 2020:" % (stock_choice,forecast_window))
	plot_graph(forecast, forecast_window_int, a, b)
