#For multiple sectors
class Tickers:
    def __init__(self):
        self.tickers_all_Sectors = [

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

        self.tickers_Banking = [

                    "HDFCBANK.NS",
                    "ICICIBANK.NS",
                    "AXISBANK.NS",
                    "KOTAKBANK.NS"
        ]

        self.tickers_it = [
                    "TCS.NS",
                    "INFY.NS",
                    "HCLTECH.NS",
                    "TECHM.NS"
        ]

        self.tickers_pharma = [
                    "SUNPHARMA.NS",
                    "CIPLA.NS"
        ]
        self.sectors = [self.tickers_all_Sectors,self.tickers_Banking,self.tickers_it,self.tickers_pharma]

    def tickers_with_sectors(self):
        return self.sectors
