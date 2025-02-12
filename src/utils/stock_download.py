import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def get_date(days:int) -> tuple[str, str]:
    today = datetime.today()
    dates = []
    for i in range(days * 2):
        date = today + timedelta(days=i)
        if date.weekday() < 0:
            dates.append(date)
            if len(dates) == days:
                break
    return dates[-1].strftime('%Y-%m-%d'), dates[0].strftime('%Y-%m-%d')

def download_stock(ticker:str) -> pd.DataFrame:
    start_day, end_day = get_date(60)
    stocks = yf.download(ticker=ticker, start=start_day, end=end_day, multi_level_index=False)
    if len(stocks) > 60:
        stocks = stocks.iloc[-60:]
    elif len(stocks) < 60:
        raise ValueError("Não foi possível obter 60 dias úteis. Verifique os dados ou aumente a margem.")
    return stocks[['Open', 'High', 'Low', 'Volume', 'Close']]
