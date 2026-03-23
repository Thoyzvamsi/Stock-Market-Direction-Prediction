from src.source import Raw_data
from notebook.feature_engineering import Processed_Data

raw_data = Raw_data()
Raw_Data_path = raw_data.Get_data()

Processedd_Data = Processed_Data(Raw_Data_path)
Processed_Data_Path = Processedd_Data.Processesing_data()