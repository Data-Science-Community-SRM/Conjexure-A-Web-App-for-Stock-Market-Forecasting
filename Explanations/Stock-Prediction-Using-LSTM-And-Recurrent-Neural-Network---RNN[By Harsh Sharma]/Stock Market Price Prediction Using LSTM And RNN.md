# Time Series Forecasting with LSTM Neural Networks

This Python script demonstrates time series forecasting using Long Short-Term Memory (LSTM) neural networks. The code uses historical Apple Inc. (AAPL) stock price data to build and train the model, and then uses it to predict future stock prices.

## Table of Contents

1. [Importing Libraries](#importing-libraries)
2. [Data Retrieval](#data-retrieval)
3. [Data Exploration](#data-exploration)
4. [Data Visualization](#data-visualization)
5. [Data Preprocessing](#data-preprocessing)
6. [Data Scaling](#data-scaling)
7. [Data Windowing](#data-windowing)
8. [Model Creation](#model-creation)
9. [Model Training](#model-training)
10. [Data Preparation for Testing](#data-preparation-for-testing)
11. [Model Testing and Prediction](#model-testing-and-prediction)
12. [Model Evaluation](#model-evaluation)
13. [Data Visualization of Predictions](#data-visualization-of-predictions)
14. [Future Forecasting](#future-forecasting)
15. [Visualization of Future Forecast](#visualization-of-future-forecast)

## Importing Libraries

The code starts by importing necessary Python libraries, including Pandas, NumPy, Seaborn, and Matplotlib, for data analysis and visualization.

## Data Retrieval

It uses the `pandas_datareader` library to fetch historical Apple Inc. stock price data from Yahoo Finance. The data is retrieved from January 1, 2012, to June 1, 2020, and stored in a Pandas DataFrame.

## Data Exploration

The script explores the dataset by displaying its shape, which indicates the number of rows and columns, and prints the information about the DataFrame.

## Data Visualization

It uses Matplotlib and Seaborn to visualize the closing stock prices over time, creating a line plot to show the historical data.

## Data Preprocessing

The code extracts the 'Close' price column from the DataFrame and converts it into a NumPy array for further data preparation.

## Data Scaling

The script uses the `MinMaxScaler` from the `scikit-learn` library to scale the data between 0 and 1. Scaling is a common practice in deep learning to normalize input data.

## Data Windowing

It segments the training data into input sequences and target values for the LSTM model. The code creates sequences of 100 days and attempts to forecast the 101st day.

## Model Creation

The script builds an LSTM-based neural network using the Keras library. The model consists of multiple LSTM layers and a final dense layer to predict stock prices.

## Model Training

It trains the LSTM model using the training data, specifying the loss function ('mean_squared_error') and optimizer ('adam'). The training history is stored for later visualization.

## Data Preparation for Testing

The code prepares the test dataset, scaling and creating sequences similar to the training data.

## Model Testing and Prediction

The LSTM model is used to make predictions on the test dataset. Predictions are then inverse-scaled to obtain actual stock prices.

## Model Evaluation

The code calculates the Root Mean Square Error (RMSE) as a measure of prediction accuracy.

## Data Visualization of Predictions

It uses Matplotlib to create line plots showing the actual and predicted stock prices on the test data.

## Future Forecasting

The script includes code to forecast stock prices for the next 30 days. It uses a loop to iteratively predict each day's price based on the previous 100 days. The predicted prices are stored in the `list_output`.

## Visualization of Future Forecast

It plots the predicted stock prices for the next 30 days, along with the past 100 days for context.

Overall, the code provides a comprehensive example of using LSTM neural networks for time series forecasting, from data retrieval to model training and future price prediction. It also demonstrates data preprocessing, scaling, and evaluation of the model's performance.
