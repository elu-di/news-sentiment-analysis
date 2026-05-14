import nbformat as nbf

nb = nbf.v4.new_notebook()

cells = []

# Title
cells.append(nbf.v4.new_markdown_cell("# Task 3: Correlation Analysis between News Sentiment and Stock Returns"))

# Setup
cells.append(nbf.v4.new_code_cell("""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os
import glob

# Initialize VADER
analyzer = SentimentIntensityAnalyzer()

def get_sentiment(text):
    if not isinstance(text, str):
        return 0
    return analyzer.polarity_scores(text)['compound']

# Paths
data_dir = '../data/raw'
stock_files = glob.glob(os.path.join(data_dir, '*.csv'))
stock_files = [f for f in stock_files if 'raw_analyst_ratings' not in f]
news_file = os.path.join(data_dir, 'raw_analyst_ratings.csv')

print("Stock files:", stock_files)
print("News file:", news_file)"""))

# Load Stock Data and Calculate Returns
cells.append(nbf.v4.new_markdown_cell("## 1. Load Stock Data and Calculate Daily Returns"))
cells.append(nbf.v4.new_code_cell("""stocks = {}
for file in stock_files:
    ticker = os.path.basename(file).split('.')[0]
    df = pd.read_csv(file)
    
    # Handle date column
    date_col = 'Date' if 'Date' in df.columns else 'date'
    df[date_col] = pd.to_datetime(df[date_col], utc=True).dt.date
    df.set_index(date_col, inplace=True)
    df.sort_index(inplace=True)
    
    # Calculate Daily Returns
    df['Daily_Return'] = df['Close'].pct_change()
    stocks[ticker] = df[['Daily_Return']]

# Combine returns into a single DataFrame for easier merging
all_returns = []
for ticker, df in stocks.items():
    temp_df = df.copy()
    temp_df['stock'] = ticker
    all_returns.append(temp_df)

returns_df = pd.concat(all_returns).reset_index()
returns_df.rename(columns={'index': 'date', 'Date': 'date'}, inplace=True)
print("Returns sample:")
print(returns_df.head())"""))

# Load and Process News Data
cells.append(nbf.v4.new_markdown_cell("## 2. Load and Process News Sentiment"))
cells.append(nbf.v4.new_code_cell("""# Load news data - selecting only relevant columns to save memory
print("Loading news data...")
news_df = pd.read_csv(news_file, usecols=['headline', 'date', 'stock'])

# Filter for relevant stocks
relevant_stocks = list(stocks.keys())
news_df = news_df[news_df['stock'].isin(relevant_stocks)].copy()

# Parse news dates
print("Parsing news dates...")
def parse_date(date_str):
    try:
        return pd.to_datetime(date_str).date()
    except:
        try:
            return pd.to_datetime(date_str, utc=True).date()
        except:
            return None

news_df['date'] = news_df['date'].apply(parse_date)
news_df.dropna(subset=['date'], inplace=True)

# Calculate Sentiment
print("Calculating sentiment (this may take a minute)...")
news_df['sentiment'] = news_df['headline'].apply(get_sentiment)

# Aggregate sentiment by date and stock
daily_sentiment = news_df.groupby(['date', 'stock'])['sentiment'].mean().reset_index()

print("Daily sentiment sample:")
print(daily_sentiment.head())"""))

# Merge and Correlation
cells.append(nbf.v4.new_markdown_cell("## 3. Merge Data and Calculate Correlation"))
cells.append(nbf.v4.new_code_cell("""# Merge returns and sentiment
merged_df = pd.merge(returns_df, daily_sentiment, on=['date', 'stock'], how='inner')

print(f"Merged data shape: {merged_df.shape}")

# Calculate Correlation
correlation = merged_df.groupby('stock').apply(lambda x: x['Daily_Return'].corr(x['sentiment']))
print("\\nPearson Correlation by Stock:")
print(correlation)

# Overall Correlation
overall_corr = merged_df['Daily_Return'].corr(merged_df['sentiment'])
print(f"\\nOverall Correlation: {overall_corr:.4f}")"""))

# Visualization
cells.append(nbf.v4.new_markdown_cell("## 4. Visualization"))
cells.append(nbf.v4.new_code_cell("""plt.figure(figsize=(10, 6))
sns.barplot(x=correlation.index, y=correlation.values, palette='viridis')
plt.title('Correlation between News Sentiment and Daily Stock Returns')
plt.ylabel('Pearson Correlation')
plt.axhline(0, color='black', linewidth=0.8)
plt.show()

# Scatter plot for one stock
ticker_to_plot = 'AAPL'
sample_plot = merged_df[merged_df['stock'] == ticker_to_plot]
plt.figure(figsize=(10, 6))
sns.regplot(data=sample_plot, x='sentiment', y='Daily_Return', scatter_kws={'alpha':0.3}, line_kws={'color':'red'})
plt.title(f'Sentiment vs Daily Returns for {ticker_to_plot}')
plt.grid(True, alpha=0.3)
plt.show()"""))

nb['cells'] = cells

with open('notebooks/task3_correlation_analysis.ipynb', 'w') as f:
    nbf.write(nb, f)

print("Notebook generated: notebooks/task3_correlation_analysis.ipynb")
