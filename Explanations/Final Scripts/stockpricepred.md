# Stock Price Forecasting Web Application

This Python script uses the Streamlit library to create a web application for stock price forecasting. It allows users to select a company's stock (Alphabet - GOOGL or Apple - AAPL), choose a forecasting period (1 to 5 weeks), and view historical stock price data along with a forecasted stock price graph.

## Table of Contents

1. [Imported Libraries](#imported-libraries)
2. [Cover Image](#cover-image)
3. [Title and Markdown](#title-and-markdown)
4. [Data Paths](#data-paths)
5. [Load Model Functions](#load-model-functions)
6. [Load Data Function](#load-data-function)
7. [Mapping Function](#mapping-function)
8. [Windowing Functions](#windowing-functions)
9. [Plotting Functions](#plotting-functions)
10. [Main Function](#main-function)

## Imported Libraries

The code imports several Python libraries, including Streamlit, NumPy, Pandas, Matplotlib, TensorFlow, and other related modules. These libraries are used for data manipulation, visualization, and machine learning.

## Cover Image

The code loads an image ('image.jpeg') and displays it using the `st.image` function from Streamlit, setting it to use the column width.

## Title and Markdown

It sets the title and introductory text for the web application using the `st.title` and `st.markdown` functions. The markdown section explains the purpose of the application and the machine learning model used for stock price forecasting.

## Data Paths

Paths to CSV files ('data_googl.csv' and 'data_aapl.csv') are defined, but these paths are not used in the provided code.

## Load Model Functions

Two functions, `load_model` and `load_model_app`, are defined to load pre-trained machine learning models based on the user's choice of a forecasting period (1 to 5 weeks). These models are built using TensorFlow/Keras and are used for making stock price forecasts.

## Load Data Function

The `load_data` function uses Streamlit's `@st.cache` decorator to read data from CSV files. It returns a Pandas DataFrame with the loaded data. The `nrows` parameter allows limiting the number of rows to load, but it's not used in the code.

## Mapping Function

The `mapper` function maps user-selected forecasting periods (e.g., '1 week') to corresponding integer values (e.g., 7).

## Windowing Functions

Several functions (`windowed_dataset`, `windowed_dataset1`, `windowed_dataset2`, `windowed_dataset3`, and `windowed_dataset4`) are defined to create windowed datasets for time series data. These datasets are used for training and testing machine learning models.

## Plotting Functions

The `plot_graph` and `future_predicted` functions are responsible for plotting stock price graphs. `plot_graph` plots the final forecasted stock prices, and `future_predicted` plots the predicted values.

## Main Function

The main part of the code is wrapped in an `if __name__ == "__main__":` block. It allows users to select either Alphabet (GOOGL) or Apple (AAPL) stock data and choose a forecasting period. Depending on the user's choices, the code downloads historical stock price data using Yahoo Finance, preprocesses the data (scaling and windowing), loads a pre-trained machine learning model, and generates stock price forecasts. The forecasted data is plotted using the `plot_graph` function.

Overall, this code creates a Streamlit web application for stock price forecasting, providing users with the ability to choose a stock, set a forecasting period, and view historical and forecasted stock price data. The code integrates machine learning models to generate forecasts based on the chosen parameters.
