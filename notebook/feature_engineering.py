import pandas as pd
from ta.momentum import RSIIndicator

class Processed_Data:
    def __init__(self,Raw_Data_path):
        self.Raw_Data_path = Raw_Data_path
    
    def Processesing_data(self):
        data = pd.read_csv(self.Raw_Data_path)

        data["Date"] = pd.to_datetime(data["Date"])
        data = data.set_index("Date")

        #Calculating Rsi in the window of 14
        data["RSI"] = data["Close"].transform(
        lambda x: RSIIndicator(close=x, window=14).rsi())

        #Adding moving averages of 25 and 50
        data["ema_14"] = data["Close"].ewm(alpha=1/25).mean()
        data["ema_25"] = data["Close"].ewm(alpha=1/50).mean()

        #Finding the distances between the close and ema
        data["ema_14_dis"] = (data["Close"] - data["ema_14"])/data["ema_14"]
        data["ema_25_dis"] = (data["Close"] - data["ema_25"])/data["ema_25"]

        #finding how spread the ema is , to know the momentum
        data["ema_spread"] = (data["ema_14"] - data["ema_25"]) / data["ema_25"]

        #Target 0 if todays close is less than next close and 1 if the opposite
        data["Target"] = (data["Close"] < data["Close"].shift(-1)).astype(int)

        #Droping NULL values 
        data = data.dropna()

        data.to_csv("data/Processed_data.csv")

        Processed_Data_path = "data/Processed_data.csv"

        return Processed_Data_path