# Requrements :
1 . Profitable trading model or stretagy
2 . winrate more than 52%
3 . Tested and Trained on very large datasets Mid cap and Large cap stocks

# Data Set Used
 Stocks Date used for training are Large and Mid cap stocks for stability

# Iteration 1
# Features for logistic regression :
for now i am thinking about 4 of them
1. RSI
2. ema_25_distance = (price - ema_25)/ema25
3. ema_50_distance = (price - ema_50)/ema50
4. ema_spread = (EMA25 - EMA50) / EMA50
5. Target = next day price Up(1) or Down(0) 

# Problems Faced:
1. I selected target as if last day price is lower than today's 1 if not the 0
   instead of setting target if next day is up then 1 if not 0

2. one of the first problem i faced is Model is just predicting majority class
   and 61% accuracy (i got very much excited after seeing the accuracy) Because
   (Probability Distribution : mean , min , max :0.5000619225268386 0.4987903185671936 0.5008517493880529 ) 
   the values are very near to 50 so what does model do if proba > 0.5 = 1 

# Iteration 2
# Features for logistic regression :
  Same as the last iteraion

# Problems Faced:
1. The indicators i am using currently (RSI ,ema_25_distance ,ema_50_distance ,ema_spread )
   are laggy because high usage of them and got 49% accuracy

2. running every cell manually will be exhustive even if they are experiments 
   so created pipelines to run every moving part automatically 


# it is an iterative process so we do it again and again until the accuracy got to the point i imagined

