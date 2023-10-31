# Financial Data Analysis and Machine Learning Preparation

This repository contains a Python script that performs various tasks related to financial data analysis and preparation for machine learning. Let's break down the code step by step:

## 1. Importing Libraries

- `pandas` (as `pd`): A library for data manipulation and analysis.
- `numpy` (as `np`): A library for numerical operations.
- `seaborn` (as `sns`): A data visualization library based on Matplotlib.
- `matplotlib.pyplot` (as `plt`): A library for creating visualizations and plots.
- `yfinance` (as `yf`): A library for fetching historical stock data from Yahoo Finance.
- `pandas_datareader as web`: A library for extracting data from various Internet sources, including Yahoo Finance.

## 2. `UpdateCSV` Function

The code defines a function named `UpdateCSV` with two parameters:
- `stock`: The stock symbol (default is 'GOOGL' for Google).
- `update`: A boolean flag (default is `True`) that determines whether to update the CSV file.

The function does the following:
- Downloads historical stock data for the specified stock symbol (default 'GOOGL') from July 1, 2021, to July 1, 2023, using Yahoo Finance. The data is stored in a Pandas DataFrame (`df_g`).
- If `update` is `True`, it saves the DataFrame to a CSV file named "DATA.csv" in the current working directory.
- Finally, it returns the DataFrame `df_g`.

## 3. Main Code

The `if __name__ == "__main__":` block calls the `UpdateCSV` function to update the CSV file with Google (Alphabet A Inc) stock data for the specified date range.

## 4. Data Processing

The code then demonstrates reading the CSV file "DATA.csv" and performing some initial data processing:
- It reads the CSV file into a Pandas DataFrame (`df_g`).
- Converts the "Date" column from a string to a timestamp object using `pd.to_datetime`.
- Sets the "Date" column as the index of the DataFrame using `set_index`.

## 5. Data Visualization

Next, it plots the "Open," "Close," and "High" stock prices over time using Matplotlib.

## 6. Summary Statistics

The `df_g.describe()` function is used to provide summary statistics of the DataFrame, such as count, mean, standard deviation, minimum, and maximum values for each column.

## 7. Data Shape

`df_g.shape` is used to print the shape of the DataFrame, indicating the number of days and features (585 days and 6 stock features).

## 8. Utility Functions

The code defines two utility functions:
- `ConvToNpaArr`: Converts a DataFrame to a NumPy array. Useful for machine learning preprocessing.
- `NormalisingData`: Normalizes data using Min-Max scaling. Takes an array as input and scales all data points to be within the range [0, 1].

## 9. Data Normalization

The script then converts the DataFrame `df_g` to an array and normalizes the data using the defined functions. The normalized data is stored in the variable `Scaled_data`.

## 10. Data Visualization (Normalized)

It plots the first 10 rows of the normalized data.

## 11. Train-Test Split

The script performs a train-test split on the normalized data:
- `train_ind` calculates the index for an 80:20 split (80% training and 20% testing).
- It creates two arrays, `train_scaled_data` and `test_scaled_data`, for training and testing data, respectively.

## 12. Data Set Sizes

It prints the size of the training and testing datasets.

This code is essentially a data preparation and exploration pipeline for a machine learning project that involves stock price prediction. It downloads historical stock data, processes it, normalizes it, and splits it into training and testing sets for further analysis and modeling.
