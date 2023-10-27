# Stock Price Forecasting Web Application

This repository contains a Python script for a Streamlit web application that provides stock price forecasting for Alphabet Inc. (GOOG) and Apple Inc. (AAPL). The application uses historical stock price data and deep learning models to predict future stock prices.

## Table of Contents
1. [Importing Libraries](#importing-libraries)
2. [Streamlit Page Configuration](#streamlit-page-configuration)
3. [Displaying an Image](#displaying-an-image)
4. [Introduction and Description](#introduction-and-description)
5. [Loading Models and Data](#loading-models-and-data)
6. [Mapping Function](#mapping-function)
7. [Windowing Functions](#windowing-functions)
8. [Plotting Function](#plotting-function)
9. [Forecast Function](#forecast-function)
10. [Main Application](#main-application)

### Importing Libraries

The script starts by importing various Python libraries, including Streamlit, NumPy, Pandas, Matplotlib, TensorFlow, pandas_datareader, scikit-learn, and yfinance.

### Streamlit Page Configuration

The `st.set_page_config` function is used to configure the Streamlit web page with a title and an icon.

### Displaying an Image

An image (probably a logo or cover image) is displayed on the web page using the `st.image` function.

### Introduction and Description

The script introduces the application with a title, a header, and multiple Markdown descriptions explaining what the application does, including the use of TensorFlow and Keras for building LSTM models for stock price forecasting.

### Loading Models and Data

Functions are defined to load different pre-trained deep learning models based on the user's choice. These models are used for stock price forecasting. Models are loaded based on the forecast window (e.g., 1 week, 2 weeks) selected by the user. A caching decorator `@st.cache_data` is applied to the `load_data` function to cache the data, reducing data loading time.

### Mapping Function

The `mapper` function maps the user's selection of the forecast window (e.g., '1 week') to the corresponding number of days (e.g., 7 days).

### Windowing Functions

Several functions (`windowed_dataset`, `windowed_dataset1`, `windowed_dataset2`, `windowed_dataset3`, and `windowed_dataset4`) are defined to create windowed datasets from the input data. These datasets are used for training and testing the deep learning models. The window size, prediction day, batch size, and shuffle buffer parameters can be adjusted.

### Plotting Function

The `plot_graph` function is used to plot the actual stock price data and the model's predicted stock prices. The plotting varies depending on the selected forecast window.

### Forecast Function

The `future_predicted` function takes a test batch and uses a pre-trained model to make predictions. It then plots the actual and predicted values for a specified number of days.

### Main Application

The main part of the script is inside an `if __name__ == "__main__":` block. Users can choose to view historical data for Alphabet (GOOG) or Apple (AAPL) stock prices. The selected stock's historical data is displayed using a line chart. Users can select a forecast window (e.g., 1 week, 2 weeks). The historical stock price data is preprocessed, scaled, and windowed based on the forecast window. The appropriate pre-trained model is loaded based on the user's choices, and the model is used to make predictions for the selected forecast window. The predictions are then plotted, showing both actual and forecasted stock prices.

This Streamlit web application provides a user-friendly interface for stock price forecasting and visualization for Alphabet (GOOG) and Apple (AAPL) based on the selected forecast period. Users can interact with the app to explore historical data and future price predictions.
