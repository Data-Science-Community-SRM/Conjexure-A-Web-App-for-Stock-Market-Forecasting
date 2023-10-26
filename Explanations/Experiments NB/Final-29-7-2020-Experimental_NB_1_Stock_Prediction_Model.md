# Time Series Forecasting with Deep Learning (LSTM)

The provided code is a detailed implementation for time series forecasting using deep learning models, specifically Long Short-Term Memory (LSTM) networks. This README will walk you through the code's functionality and structure step by step.

## Data Preparation and Exploration
1. The code starts by importing necessary libraries like NumPy, Pandas, TensorFlow, and Matplotlib.
2. It uses the `pandas_datareader` library to fetch historical stock price data for Google (GOOGL) from Yahoo Finance, covering the time period from April 1, 2003, to July 15, 2020.
3. It then prints the DataFrame containing the fetched data and plots the 'High' prices.

## Data Scaling
4. The code uses Min-Max scaling (feature scaling) to transform the stock closing prices to a range between 0 and 0.75. Scaling helps the neural network to converge more effectively.

## Data Splitting
5. The dataset is divided into training, testing, and forecasting sets.
6. The training data includes 90% of the dataset, while the remaining 10% is used for testing.
7. A window of the last 30 days is selected as the input window size.
8. An additional 7 days are used for forecasting future stock prices.

## Data Windowing and Batching
9. The `windowed_dataset` function is defined to create windowed and batched datasets for training and testing.
10. It prepares the data by creating sequences with the specified window size and forecasting days.
11. The data is shuffled and then batched for improved training efficiency.

## Model Building
12. The code defines a deep learning model using TensorFlow's Keras API.
13. The model consists of Convolutional layers, multiple LSTM layers, and Dense layers.
14. The model is optimized for time series forecasting.
15. The model summary is printed to provide an overview of the architecture.

## Model Training
16. The model is compiled using the Adam optimizer, Huber loss function, and Mean Squared Error (MSE) as a metric.
17. It is then trained using the training dataset for a specified number of epochs.
18. The training history (loss and MSE) is stored in `hist` for later visualization.

## Model Evaluation
19. The code provides a function `visualplotloss` to visualize the model's predictions against actual values for the test dataset.
20. The evaluation is also conducted, and the model's performance is assessed using the test dataset.

## Model Saving
21. The trained models are saved to separate files based on the forecast period (7 days, 14 days, 21 days, 28 days, 35 days).
22. This allows for future use and comparison of different forecast models.

## Data Preparation for Future Forecast
23. The code further fetches recent data from Yahoo Finance for a specific period from March 1, 2020, to July 20, 2020.
24. The 'Close' prices of this dataset are scaled using the same Min-Max scaler applied earlier.

## Model Application and Visualization
25. The code loads the previously saved models based on the user's choice of forecast window (1 week, 2 weeks, etc.).
26. It applies the selected model to predict the future stock prices based on the most recent data.
27. The predictions are then visualized alongside the actual values for the forecasting period.

This code essentially demonstrates how to preprocess, split, and forecast stock prices using deep learning techniques, specifically LSTM-based models. It provides insights into different models with varying forecasting windows and shows the prediction results graphically.
