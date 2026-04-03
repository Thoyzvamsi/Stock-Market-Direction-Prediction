import pandas as pd
from ta.momentum import RSIIndicator

class Processed_Data:
    def __init__(self,Raw_Data_path):
        self.Raw_Data_path = Raw_Data_path
    
    def Processesing_data_2(self):
        data = pd.read_csv(self.Raw_Data_path)

        data["Date"] = pd.to_datetime(data["Date"])
        data = data.sort_values(["Ticker", "Date"]).reset_index(drop=True)

        data["Returns"] = data.groupby("Ticker")["Close"].pct_change()

        data["volatility"] = data.groupby("Ticker")["Returns"].transform(lambda x: x.rolling(10).std())
        data["Volatility_ratio"] = (data["volatility"] /data.groupby("Ticker")["volatility"].transform(lambda x: x.rolling(50).mean()))

        data["momentum"] = data.groupby("Ticker")["Close"].pct_change(5)
        data["Acceleration"] = data.groupby("Ticker")["momentum"].diff()

        #stock_return = stock.pct_change()
        #market_return = index.pct_change()

        #relative_strength = stock_return - market_return
        data["volume_ma"] = data.groupby("Ticker")["Volume"].transform(lambda x: x.rolling(20).mean())
        data["Volume_spike"] = data["Volume"] / data["volume_ma"]

        data["rolling_max"] = data.groupby("Ticker")["Close"].transform(lambda x: x.rolling(20).max())
        data["rolling_min"] = data.groupby("Ticker")["Close"].transform(lambda x: x.rolling(20).min())

        data["Position"] = (data["Close"] - data["rolling_min"]) / (data["rolling_max"] - data["rolling_min"])

        data["Target"] = (data["Close"] < data["Close"].shift(-1)).astype(int)

        data = data.dropna()

        data.to_csv("data/Processed_data.csv")
        Processed_Data_path = "data/Processed_data.csv"

        return Processed_Data_path