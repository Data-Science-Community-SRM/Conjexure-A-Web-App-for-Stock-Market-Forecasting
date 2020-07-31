# Web app for stock prices

Option to select Stock Symbol  
Number of days to be predicted in the future

Has Acess to a NoSQl database which has data like
> Date - stock - No. of days selection - Values

Web app plots a graph with lines -

* Real Stock value from the pandas datareader till current day
* Prediction value for the next whatever days choosen 
* (Future) previously predicted values

### When user loggs in the app and chooses to look at graph

web app opens database grabs appropriate values
opens stock csv grabs market data till that day
presents to user

### Script to run models and update database
Load all the model one by one
Update the csv with currebt data till that day
Take the last 30,60,90 days values and predict for the next 7,14,21 days add this to database

Needs pretrained models for every stock symbol config ability to add models

