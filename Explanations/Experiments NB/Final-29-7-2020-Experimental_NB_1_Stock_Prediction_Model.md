# Time Series Forecasting with Deep Learning Models

This code is a Python script for time series forecasting using various deep learning models, specifically Convolutional and Recurrent Neural Networks (CNNs and LSTMs). It is used for predicting stock prices. Let's break down the code step by step:

## 1. Importing Libraries
- `numpy` (as `np`): NumPy is a popular library for numerical operations in Python.
- `pandas_datareader`: A library for fetching financial data from various sources.
- `pandas` (as `pd`): Pandas is a data manipulation library.
- `tensorflow` (as `tf`): TensorFlow is an open-source machine learning framework.
- `matplotlib.pyplot` (as `plt`): Matplotlib is a library for creating visualizations.
- `yfinance` (as `yf`): This library is used for downloading financial data from Yahoo Finance.

## 2. Data Retrieval
- The code uses Yahoo Finance (`yf.download`) to fetch historical stock price data for Google (GOOGL) from July 1, 2015, to July 1, 2023, and stores it in the `df_g` variable.
- The retrieved data is printed to the console using `print(df_g)`.

## 3. Data Preprocessing
- Min-Max scaling is applied to the "Close" price data from `df_g` to transform it to a range between 0 and 0.75.
- The time series data is reshaped into a suitable format for input to a neural network.
- The data is split into training, testing, and forecast datasets based on the specified window size and prediction day (in this case, 30 days for training and 7 days for testing and forecasting).

## 4. Data Batching
- The `windowed_dataset` function is defined to create TensorFlow data pipelines for training and testing data.
- Training and testing data are split into batches using this function.

## 5. Model Building
- A deep learning model is defined using TensorFlow's Keras API. The model consists of several layers, including Convolutional 1D (Conv1D) and Long Short-Term Memory (LSTM) layers.
- The model is compiled with an optimizer, loss function, and metrics.
- Model training is performed with a specified number of epochs, and the training history is saved in the `hist` variable.

## 6. Model Evaluation and Visualization
- The code then evaluates the model using the test dataset and plots the training and validation loss and mean squared error for visualization.
- It also generates predictions on the test dataset and plots the actual vs. predicted values for a sample.

## 7. Saving the Model
- The trained model is saved to an H5 file using the `model.save` function.

## 8. Additional Models
- The code defines and trains additional models (Model 2, Model 3, Model 4, and Model 5) using similar procedures, with varying window sizes and prediction day values.
- These models are evaluated and saved in a manner similar to the first model.

## 9. Download of Additional Test Data
- The code downloads additional test data from Yahoo Finance for the specified date range.

## 10. Visualizing Model Predictions on New Test Data
- The code visualizes the predictions made by each of the five models on the new test data.

In summary, this code fetches historical stock price data, preprocesses it, trains five different models for time series forecasting with varying time windows and prediction horizons, evaluates the models, and saves them. It also demonstrates the model predictions on new test data.
