import yfinance as yf
import pandas as pd

def get_option_chain(ticker, max_expirations=3):
    stock = yf.Ticker(ticker)
    expirations = stock.options[:max_expirations]
    all_options = []
    for date in expirations:
        chain = stock.option_chain(date)
        calls = chain.calls.copy()
        calls['expirationDate'] = date
        calls['optionType'] = 'call'
        puts = chain.puts.copy()
        puts['expirationDate'] = date
        puts['optionType'] = 'put'
        all_options.extend([calls, puts])
    df = pd.concat(all_options, axis=0)
    df.reset_index(drop=True, inplace=True)
    return df

def compute_iv(df, spot, r, pricing_func):
    df['expirationDate'] = pd.to_datetime(df['expirationDate'])
    df['T'] = (df['expirationDate'] - pd.Timestamp.today()).dt.days / 365.0
    df['mid'] = (df['bid'] + df['ask']) / 2
    df['impliedVolatility'] = df.apply(
        lambda row: pricing_func(row['mid'], spot, row['strike'], row['T'], r, row['optionType'])
        if row['T'] > 0 and row['mid'] > 0 else pd.NA,
        axis=1
    )
    return df
