# Conjexure

Conjexure is a machine learning web app for forecasting the stock prices of certain companies into the future.

## Description
Conjexure utilizes the stock symbols for Alphabet Inc. (GOOGL) and Apple Inc (AAPL) and can forecast into a user-specified future window of 1-5 weeks. It also displays the raw data for the user to inspect. For the stock price, the closing price of a stock on any given day is chosen.

For deployment of Conjexure as an interactive web app, the [Streamlit](https://www.streamlit.io) framework was chosen for its robustness and ease of scripting.

You may go through the documentation for Streamlit [here.](https://docs.streamlit.io/en/stable/)


## Getting Started

To play around with Conjexure yourself, head on to our web app at

### Running on a local machine
#### Prerequisites

To run Conjexure on your local machine, first ensure that the following relevant dependencies are installed.

1. [Pandas_datareader](https://pandas-datareader.readthedocs.io/en/latest/)
2. [Pandas](https://pandas.pydata.org)
3. [NumPy](numpy.org)
4. [Matplotlib.pyplot](https://matplotlib.org/api/pyplot_api.html)

To install streamlit, use the given pip command.
```bash
pip install streamlit
```
### Running 
Download the zip file from our repository and unzip into the desired directory.

Running Streamlit scripts is amazingly easy. All you need to do is enter the following line in your terminal.

```bash
streamlit run stockpricepred.py
```

## Machine Learning Architecture

Conjexure uses the Tensorflow and Keras libraries to build 5 stacked LSTM models complemented by a convolutional as well as a lambda layer.

There are 5 models to forecast into 5 different future windows (from 1-5 weeks) depending on user specification. Each model utilizes a proportionately larger training set to compensate for the increasing prediction window. For example, the model to forecast one week into the future uses the last 30 days of stock price data, the model to forecast two weeks uses the last 60 days of data and so on.

For any stock symbol, up to 5 different price metrics are available, including the opening price, the closing price, the high, the low, etc. Conjexure uses the closing price as the standard stock price. We came to this decision because the closing price accounts for news related to the company and the market's general mood on the day (which can then be predicted by our model.)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
