import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd
import os

# Create the PDF document
pdf_path = r'c:\Users\hp\Documents\WEEK-1\news-sentiment-analysis\Nova_Financial_Report.pdf'

def create_report():
    with PdfPages(pdf_path) as pdf:
        # --- PAGE 1: TITLE PAGE ---
        plt.figure(figsize=(8.5, 11))
        plt.axis('off')
        plt.text(0.5, 0.7, 'Nova Financial Solutions', fontsize=28, ha='center', fontweight='bold', color='#1a5f7a')
        plt.text(0.5, 0.6, 'Predicting Price Moves with News Sentiment', fontsize=18, ha='center', color='#333333')
        plt.text(0.5, 0.5, '10 Academy Week 1 Challenge - Final Report', fontsize=14, ha='center', style='italic')
        plt.text(0.5, 0.4, 'May 2026', fontsize=12, ha='center')
        plt.text(0.5, 0.1, 'Publication-Style Analysis of Sentiment and Technical Indicators', fontsize=10, ha='center', color='gray')
        pdf.savefig()
        plt.close()

        # --- PAGE 2: EXECUTIVE SUMMARY & METHODOLOGY ---
        plt.figure(figsize=(8.5, 11))
        plt.axis('off')
        plt.text(0.1, 0.9, 'Executive Summary', fontsize=16, fontweight='bold', color='#1a5f7a')
        summary = (
            "This report details the connection between financial news narratives and stock market performance. "
            "By analyzing over 1.4 million news articles and historical price data for major tech giants "
            "(AAPL, AMZN, GOOG, NVDA), we discovered a measurable positive correlation between news sentiment "
            "and daily stock returns."
        )
        plt.text(0.1, 0.8, '\n'.join([summary[i:i+80] for i in range(0, len(summary), 80)]), fontsize=11, family='serif')

        plt.text(0.1, 0.65, 'Methodology', fontsize=16, fontweight='bold', color='#1a5f7a')
        methodology = (
            "1. Exploratory Data Analysis (EDA): Understanding publication patterns.\n"
            "2. Technical Analysis: Computing SMA, EMA, RSI, and MACD.\n"
            "3. Correlation Analysis: Linking VADER sentiment scores to daily stock returns."
        )
        plt.text(0.1, 0.55, methodology, fontsize=11, family='serif')
        pdf.savefig()
        plt.close()

        # --- PAGE 3: CORRELATION RESULTS ---
        plt.figure(figsize=(8.5, 11))
        plt.axis('off')
        plt.text(0.1, 0.9, 'Correlation Analysis Results', fontsize=16, fontweight='bold', color='#1a5f7a')
        
        # Data for table
        data = {
            'Stock': ['NVDA', 'GOOG', 'AMZN', 'AAPL'],
            'Same-Day Corr': [0.2148, 0.1895, 0.1668, 0.1239],
            'Lag Corr (Prev Day)': [-0.0242, -0.0097, -0.2877, -0.2078]
        }
        df = pd.DataFrame(data)
        
        # Draw table
        table = plt.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center')
        table.auto_set_font_size(False)
        table.set_fontsize(11)
        table.scale(1.2, 2.5)
        
        plt.text(0.1, 0.25, "Key Insight:", fontsize=12, fontweight='bold')
        insight = (
            "The positive same-day correlation vs. negative/zero lag correlation suggests "
            "that markets are highly efficient. Sentiment is priced in almost immediately, "
            "leaving little predictive value for the next trading day."
        )
        plt.text(0.1, 0.15, '\n'.join([insight[i:i+80] for i in range(0, len(insight), 80)]), fontsize=11)
        pdf.savefig()
        plt.close()

        # --- PAGE 4: STRATEGIES & CONCLUSION ---
        plt.figure(figsize=(8.5, 11))
        plt.axis('off')
        plt.text(0.1, 0.9, 'Actionable Investment Strategies', fontsize=16, fontweight='bold', color='#1a5f7a')
        strategies = (
            "- Sentiment-Filtered Breakouts: Use Sentiment > 0.2 to confirm SMA crossovers.\n"
            "- The 'Hype' Warning: Be cautious if RSI > 70 and Sentiment is extremely high.\n"
            "- Earnings Front-Running: Monitor sentiment 2-3 days before earnings calls."
        )
        plt.text(0.1, 0.75, strategies, fontsize=11, family='serif')
        
        plt.text(0.1, 0.5, 'Conclusion', fontsize=16, fontweight='bold', color='#1a5f7a')
        conclusion = (
            "Integrating qualitative sentiment with quantitative indicators provides a holistic view "
            "of market dynamics. At Nova Financial Solutions, we leverage this dual-approach to "
            "build robust predictive models."
        )
        plt.text(0.1, 0.4, '\n'.join([conclusion[i:i+80] for i in range(0, len(conclusion), 80)]), fontsize=11)
        
        plt.text(0.5, 0.05, 'Nova Financial Solutions - Confidential', fontsize=8, ha='center', color='gray')
        pdf.savefig()
        plt.close()

    print(f"PDF Report generated: {pdf_path}")

if __name__ == '__main__':
    create_report()
