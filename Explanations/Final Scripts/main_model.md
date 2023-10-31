# Stock Market Data Analysis using Neural Networks

The provided code is a Python script that demonstrates the process of creating, training, and evaluating a neural network model for time series forecasting. It primarily uses TensorFlow and several related libraries for this purpose.

## Table of Contents

1. [Importing Libraries](#importing-libraries)
2. [Data Download and Scaling](#data-download-and-scaling)
3. [Data Preparation](#data-preparation)
4. [Windowed Dataset Function](#windowed-dataset-function)
5. [Neural Network Model](#neural-network-model)
6. [Model Compilation](#model-compilation)
7. [Model Training](#model-training)
8. [Plotting Performance](#plotting-performance)
9. [Forecasted Plots](#forecasted-plots)
10. [Model Evaluation](#model-evaluation)

## Importing Libraries

- The code begins by importing necessary Python libraries, including NumPy for numerical operations, Pandas for data manipulation, TensorFlow for building the neural network, Matplotlib for plotting, and Yahoo Finance (yfinance) for downloading historical stock price data.

## Data Download and Scaling

- The code downloads historical stock price data for Alphabet Inc. (GOOG) using Yahoo Finance and selects data from a specified date range.
- It then performs data scaling using the Min-Max scaling technique, transforming the closing price data into a scaled series. This scaling is important for training neural networks.

## Data Preparation

- The data is split into training and test sets, with 90% used for training and 10% for testing. This split is based on the `Trainsplit` variable.
- The training and test data are further divided into windows of a fixed size, which are used as input features for the neural network. `Window` represents the size of the window (number of past days), and `Predday` is the number of days to predict into the future.
- A separate set of data (`closeforecast`) is reserved for forecasting future prices.

## Windowed Dataset Function

- The `windowed_dataset` function is defined to create fixed-size batches of data suitable for training the neural network. It performs the following steps:
  - Creates a TensorFlow dataset from the input series.
  - Divides the data into overlapping windows of specified size and shift.
  - Shuffles the data for better training.
  - Maps the data to separate input and output (prediction) batches.

## Neural Network Model

- The code defines a neural network model using TensorFlow's Keras API. The model architecture includes:
  - A 1D Convolutional layer with ReLU activation for capturing patterns in the time series.
  - Multiple LSTM (Long Short-Term Memory) layers for handling sequential data.
  - Dense layers with SELU (Scaled Exponential Linear Unit) activation functions.
  - The model's summary is printed, showing layer details.

## Model Compilation

- The model is compiled with an optimizer (Adam), loss function (Huber loss), and metric (mean squared error). This prepares the model for training.

## Model Training

- The model is trained using the training data (`trainbatches`) for a specified number of epochs (100 in this case).
- Training and validation metrics, such as loss and mean squared error (mse), are recorded and stored in `hist`.

## Plotting Performance

- The code plots the training and validation loss and mean squared error (mse) over epochs to visualize the model's performance.

## Forecasted Plots

- The `visualplotloss` function is defined to generate plots that compare the model's predictions with actual values for the next 7 days. It does this for a subset of the test data.

## Model Evaluation

- Finally, the code evaluates the model's performance using the test data (`testbatches`) and prints the evaluation results, which typically include the loss and other metrics.

This code provides a comprehensive example of how to create and train a neural network model for time series forecasting. It covers data preprocessing, model architecture, training, and evaluation, making it a valuable reference for tasks involving time series prediction.
