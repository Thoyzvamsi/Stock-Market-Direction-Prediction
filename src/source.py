import yfinance as yf
import pandas as pd

class Raw_data:
    def __init__(self,tickers ):
        self.tickers = tickers
        
    def Get_data(self):
        dt = yf.download("TCS.NS",start="2024-01-01")

        clean_list = []

        for ticker in self.tickers:
            df = yf.download(
                ticker,
                start="2010-01-01",
                end="2025-12-31",
                interval="1d",
                progress=False
            )
            
            if not df.empty:
                # 1. Flatten columns (fix multi-index)
                df.columns = [col[0] if isinstance(col, tuple) else col for col in df.columns]
                
                # 2. Remove duplicate columns
                df = df.loc[:, ~df.columns.duplicated()]
                
                # 3. Reset index → bring Date as column
                df = df.reset_index()
                
                # 4. Add ticker column
                df["Ticker"] = ticker
                
                # 5. Force consistent column order
                df = df[["Date", "Close", "High", "Low", "Open", "Volume", "Ticker"]]
                
                clean_list.append(df)

        # Final concat
        data = pd.concat(clean_list, ignore_index=True)
        data = data.set_index("Date",drop=True)
        data.to_csv("data/Raw_data.csv")
        path = "data/Raw_data.csv"

        return path