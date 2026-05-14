import pandas as pd
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os
import glob

analyzer = SentimentIntensityAnalyzer()

def parse_date(date_str):
    try:
        return pd.to_datetime(date_str).date()
    except:
        try:
            return pd.to_datetime(date_str, utc=True).date()
        except:
            return None

data_dir = 'data/raw'
stock_files = glob.glob(os.path.join(data_dir, '*.csv'))
stock_files = [f for f in stock_files if 'raw_analyst_ratings' not in f]
news_file = os.path.join(data_dir, 'raw_analyst_ratings.csv')

stocks = {}
all_returns = []
for file in stock_files:
    ticker = os.path.basename(file).split('.')[0]
    df = pd.read_csv(file)
    date_col = 'Date' if 'Date' in df.columns else 'date'
    df[date_col] = pd.to_datetime(df[date_col], utc=True).dt.date
    df.set_index(date_col, inplace=True)
    df.sort_index(inplace=True)
    df['Daily_Return'] = df['Close'].pct_change()
    stocks[ticker] = df[['Daily_Return']]
    
    temp_df = df[['Daily_Return']].copy()
    temp_df['stock'] = ticker
    all_returns.append(temp_df)

returns_df = pd.concat(all_returns).reset_index()
returns_df.rename(columns={'Date': 'date', 'index': 'date'}, inplace=True)

print("Loading news...")
news_df = pd.read_csv(news_file, usecols=['headline', 'date', 'stock'])
news_df = news_df[news_df['stock'].isin(stocks.keys())].copy()
print("Parsing news dates...")
news_df['date'] = news_df['date'].apply(parse_date)
news_df.dropna(subset=['date'], inplace=True)

print("Calculating sentiment...")
news_df['sentiment'] = news_df['headline'].apply(lambda x: analyzer.polarity_scores(str(x))['compound'])
daily_sentiment = news_df.groupby(['date', 'stock'])['sentiment'].mean().reset_index()

merged_df = pd.merge(returns_df, daily_sentiment, on=['date', 'stock'], how='inner')

print("\nPearson Correlation by Stock:")
print(merged_df.groupby('stock').apply(lambda x: x['Daily_Return'].corr(x['sentiment'])))

print("\nSample counts:")
print(merged_df.groupby('stock').size())
