from src.source import Raw_data
from notebook.feature_engineering import Processed_Data
from notebook.logistic_reg import Logistic_regression

tickers = [
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
        ]

raw_data = Raw_data(tickers)
Raw_Data_path = raw_data.Get_data()

Processedd_Data = Processed_Data(Raw_Data_path)
Processed_Data_Path = Processedd_Data.Processesing_data_2()

Model_Fitting = Logistic_regression(Processed_Data_Path)
accuracy,cm,Classification_report = Model_Fitting.Logistic_Reg()

print("Accuracy :",accuracy)
print("cm :", cm)
print("cf :", Classification_report)


