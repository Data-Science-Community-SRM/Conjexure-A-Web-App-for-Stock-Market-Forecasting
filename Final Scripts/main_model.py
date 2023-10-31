#Importing Important Libraries

import numpy as np
import pandas_datareader as web
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
import yfinance as yf

# using JD as its not as stable
df_g=yf.download('GOOG', start='2021-10-10', end='2023-10-10')


#SCALING :
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0,0.75))# 0.75 so it's easier for selu to reach
# closing values - feature From Dataset
ser = df_g.Close.values
ser = ser.reshape(-1,1)
# scaled series
series = scaler.fit_transform(ser)



# Getting Ready For Fixed Batches and and for look up of fixed past days
# fixed input size to model, last 30 days
Window = 30
Predday = 7

# To split the data into 90:10
Trainsplit = 0.9

cut = int(series.shape[0]*Trainsplit)

# train
closetrain = series[:cut]
# test
closetest = series[cut:-(Window+Predday)]
# forecast for future 7 days
closeforecast = series[-(Window+Predday):]



# Specific Function to Create a Fixed batch with params
def windowed_dataset(series, window_size = 31,predday = 7, batch_size = 32, shuffle_buffer= 1000):
    ds = tf.data.Dataset.from_tensor_slices(series)
    ds = ds.window(window_size + predday, shift=1, drop_remainder=True)
    ds = ds.flat_map(lambda w: w.batch(window_size + predday))
    ds = ds.shuffle(shuffle_buffer)
    ds = ds.map(lambda w: (w[:-7], tf.squeeze(w[-7:])))
    return ds.batch(batch_size).prefetch(3)

trainbatches =  windowed_dataset(closetrain)
testbatches =  windowed_dataset(closetest,batch_size=8)



#Main Neural Network Model Layer Arch

from tensorflow.keras import layers

tf.keras.backend.clear_session()

tf.random.set_seed(7)
np.random.seed(7)

model = tf.keras.Sequential()
model.add(layers.Conv1D(128,5,1,padding = "causal",activation = "relu",input_shape=[None, 1]))
for j in [128,128]:
    model.add(layers.LSTM(j, return_sequences=True))
model.add(layers.LSTM(128))
for i in [64,64,7]:
    model.add(layers.Dense(i, activation="selu"))

print(model.summary())


#optimizer = tf.keras.optimizers.SGD(lr=1e-2, momentum=0.9)
#kl = l = tf.keras.losses.LogCosh()

model.compile(optimizer = 'adam', loss =tf.keras.losses.Huber(), metrics=["mse"])
h = model.fit(trainbatches,epochs=100,validation_data=testbatches,verbose=1)
hist = h.history


#To Get Plots of Performance :

for i in ["loss","mse"]:
    plt.plot(hist[i],label = i)
    plt.plot(hist["val_"+i],label = "val_"+i)
    plt.legend()
    plt.show()


#Getting Next Days Forecasted Plots :

def visualplotloss(dataset):
    x,y = next(iter(dataset))
    output = model.predict(x)
    timecorr =list(range(30,37))
    for j in range(8):
        plt.ylim(0,0.75)
        plt.plot(x[j])
        plt.plot(timecorr,output[j],"--")
        plt.plot(timecorr,y[j])
        plt.legend(["Input of 30 days","Prediction","Truth Value"])
        plt.show()

visualplotloss(testbatches)

#For Evaluating our model :
model.evaluate(testbatches)







