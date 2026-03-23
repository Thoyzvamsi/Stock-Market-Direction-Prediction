# Requrements :
1 . Profitable trading model or stretagy
2 . winrate more than 52%
3 . Tested and Trained on very large datasets Mid cap and Large cap stocks

4. Stocks that i need for training
    "RELIANCE.NS",
    "TCS.NS",
    "INFY.NS",
    "HDFCBANK.NS",
    "ICICIBANK.NS",
    "AXISBANK.NS",
    "KOTAKBANK.NS",
    "HCLTECH.NS",
    "TECHM.NS",
    "SUNPHARMA.NS",
    "CIPLA.NS",
    "PIDILITIND.NS",
    "COLPAL.NS",
    "BHARTIARTL.NS",
    "LT.NS",
    "MARUTI.NS",
    "ITC.NS,"
    "HINDUNILVR.NS",
    "ULTRACEMCO.NS",
    "POWERGRID.NS",
    "NTPC.NS",
    "SBIN.NS",
    "DIVISLAB.NS",
    "BAJAJ-AUTO.NS"

# accuracy given by ai model is too less (51%) so i am preparing my own feature set

# Features for logistic regression :

for now i am thinking about 4 of them
1. RSI
2. ema_25_distance = (price - ema_25)/ema25
3. ema_50_distance = (price - ema_50)/ema50
4. ema_spread = (EMA25 - EMA50) / EMA50

5. Target = next day price Up(1) or Down(0) 

Features used to train is 1,2,3,4 

# it is an iterative process so we do it again and again until the accuracy is higher

