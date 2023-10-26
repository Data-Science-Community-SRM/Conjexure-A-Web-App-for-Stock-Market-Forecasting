# Stock Market Data Analysis with LSTM

This Python script is designed for time series forecasting using a Long Short-Term Memory (LSTM) neural network. It provides a detailed explanation of its functionality, structure, and the relevant programming concepts and libraries used.

## Table of Contents
1. [Importing Libraries](#importing-libraries)
2. [Loading Data](#loading-data)
3. [Data Preprocessing](#data-preprocessing)
4. [Sequence Splitting Function](#sequence-splitting-function)
5. [Data Splitting](#data-splitting)
6. [Input Sequence Creation](#input-sequence-creation)
7. [LSTM Model Setup](#lstm-model-setup)
8. [Model Summary](#model-summary)
9. [Model Training](#model-training)
10. [Model Prediction](#model-prediction)
11. [Inverse Scaling](#inverse-scaling)
12. [Performance Evaluation](#performance-evaluation)
13. [Printing RMSE](#printing-rmse)

## 1. Importing Libraries
- The code begins by importing necessary libraries, including NumPy for numerical operations, Pandas for data manipulation, Matplotlib for data visualization, and Keras for building and training neural networks.

## 2. Loading Data
- It loads a dataset from a CSV file named 'dicindia.csv' using Pandas. The dataset likely contains historical stock price data.

## 3. Data Preprocessing
- The code preprocesses the data by applying Min-Max scaling to the 'Close' column. This scaling ensures that the data values fall within the range [0, 1], which is a common practice when working with neural networks.

## 4. Sequence Splitting Function
- A function named `split_sequence` is defined to split the time series data into input sequences (X) and target values (y) based on a specified number of time steps (`n_steps`).

## 5. Data Splitting
- The dataset is divided into training and testing sets. Approximately 70% of the data is used for training, and the remaining 30% is used for testing.

## 6. Input Sequence Creation
- Input sequences for training and testing are created using the `split_sequence` function with a defined number of time steps (`timesteps`). The sequences are reshaped to fit the input shape expected by the LSTM model.

## 7. LSTM Model Setup
- A Sequential Keras model is created.
- It contains two LSTM layers with 32 units each and ReLU activation functions. The first LSTM layer returns sequences, while the second one doesn't.
- A Dense layer with one unit is added for regression, and the model is compiled using the Adam optimizer and mean squared error loss.

## 8. Model Summary
- The code prints a summary of the model's architecture, showing the number of parameters in each layer.

## 9. Model Training
- The model is trained using the training data. It runs for 100 epochs with a batch size of 30.

## 10. Model Prediction
- The trained model is used to make predictions on both the training and testing data.

## 11. Inverse Scaling
- The predicted values are inverse-transformed using the Min-Max scaling to obtain meaningful stock price predictions in their original scale.

## 12. Performance Evaluation
- The code calculates the Root Mean Squared Error (RMSE) for both the training and testing data. RMSE is a common metric for evaluating the accuracy of regression models. Lower RMSE values indicate better performance.

## 13. Printing RMSE
- The RMSE values for both training and testing data are printed to evaluate the model's performance.

In summary, this code loads a time series dataset, preprocesses it, builds an LSTM-based neural network for stock price forecasting, trains the model, and evaluates its performance using RMSE. The goal is to predict stock prices based on historical data.
