import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
import os
import time

ticker_list = ["TMO", "NKE", "PFE", "CPB", "YUMC", "TSM", "BF-B", "GSK", "GOOGL"]
end_date = datetime.today()
#print(end_date)
start_date = end_date-timedelta(days = 365)
#print(start_date)
close_df = pd.DataFrame()
for ticker in ticker_list:
    data = yf.download(ticker, start = start_date, end=end_date)
    close_df[ticker]= data["Close"]
    print(close_df)
output_folder = "/Users/soniamudarth/Desktop/Finance Python"
output_file = os.path.join(output_folder,"yfiance to download current stock data into excel.xlsx")
close_df.to_excel(output_file)







