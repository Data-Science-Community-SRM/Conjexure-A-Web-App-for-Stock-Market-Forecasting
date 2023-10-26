# Stock Price Forecasting Web Application

This Python script is a Streamlit web application that forecasts stock prices for Alphabet Inc. (GOOG) and Apple Inc. (AAPL) based on historical data. 

## Table of Contents
- [Importing Libraries](#importing-libraries)
- [Set Page Configuration](#set-page-configuration)
- [Cover Image](#cover-image)
- [Title and Introduction](#title-and-introduction)
- [Data Paths](#data-paths)
- [Loading Models](#loading-models)
- [Caching Data](#caching-data)
- [Mapping Function](#mapping-function)
- [Windowing Functions](#windowing-functions)
- [Plotting Functions](#plotting-functions)
- [Main Function](#main-function)

### Importing Libraries
The script starts by importing necessary libraries and modules, including Streamlit, NumPy, Pandas, Matplotlib, TensorFlow, Keras, pandas_datareader, scikit-learn's MinMaxScaler, and yfinance.

### Set Page Configuration
It uses `st.set_page_config` to configure the page title and icon (favicon) for the Streamlit app.

### Cover Image
The script loads and displays a cover image using `st.image`.

### Title and Introduction
It sets the title and provides introductory information about the application, its purpose, and the use of machine learning models for stock price forecasting.

### Data Paths
Specifies the paths to data files for both Alphabet (GOOG) and Apple Inc. (AAPL).

### Loading Models
Defines two functions, `load_model` and `load_model_app`, to load pre-trained machine learning models based on the user's choice of a forecast window (1 week, 2 weeks, etc.). These models are loaded using Keras.

### Caching Data
The `@st.cache_data` decorator is used to cache data loading, ensuring that data is only loaded once and cached for subsequent use.

### Mapping Function
Defines a mapping function, `mapper`, to map user-friendly forecast window strings to the corresponding number of days.

### Windowing Functions
Defines several windowing functions (`windowed_dataset`, `windowed_dataset1`, `windowed_dataset2`, `windowed_dataset3`, and `windowed_dataset4`) to create TensorFlow datasets for model training and prediction.

### Plotting Functions
Two plotting functions, `plot_graph` and `future_predicted`, are defined for plotting forecasted stock prices. They use Matplotlib for creating line graphs.

### Main Function
The main part of the script is enclosed in an `if __name__ == "__main__":` block.
- It allows users to choose between Alphabet (GOOG) and Apple Inc. (AAPL).
- Users can view raw data and select a forecast window (1 week, 2 weeks, etc.).
- Historical stock price data is downloaded using yfinance based on the user's choice.
- The selected data is displayed as a line chart using `st.line_chart`.
- Users can choose a forecast window for future price predictions.
- After preprocessing the data, including scaling and windowing, the appropriate model is loaded using the `load_model` or `load_model_app` function.
- Predictions are made and displayed using the `plot_graph` function.

This code effectively creates an interactive web application for stock price forecasting, allowing users to select the stock of interest, view historical data, and receive forecasts for different time periods.
