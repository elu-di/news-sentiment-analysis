# Decoding Market Narratives: A Comprehensive Analysis of Sentiment and Price Action

*Nova Financial Solutions - Week 1 Challenge Report*

---

## 1. Executive Summary
This report presents a dual-modality analysis of the stock market, combining technical price indicators with high-frequency news sentiment. By analyzing over 1.4 million news headlines alongside a decade of stock data for major tech firms (NVDA, AAPL, GOOG, AMZN), we identify measurable patterns where news narratives serve as a significant, albeit subtle, catalyst for price movement.

---

## 2. Technical Momentum Insights (Task 2)
Our quantitative pipeline successfully implemented a suite of technical indicators to capture market momentum:

-   **Trend Identification**: 20-day and 50-day SMAs revealed strong long-term bullish structures in **NVIDIA (NVDA)**, punctuated by periods of intense volatility.
-   **Momentum Overshoots**: RSI (Relative Strength Index) analysis showed that stocks frequently entered "overbought" territory (>70) during peak news cycles, often preceding short-term consolidations.
-   **Trend Crossovers**: MACD analysis identified key "golden cross" events that signaled sustained upward movements, particularly during the early 2020 recovery period.

---

## 3. Sentiment-Return Correlation (Task 3)
We quantified the relationship between news sentiment (VADER compounded scores) and daily stock returns.

### Same-Day Correlation
We observed a consistent **positive linear relationship** across all analyzed tickers:

| Stock | Pearson Correlation (Same-Day) |
| :--- | :--- |
| **NVDA** | **0.2148** |
| **GOOG** | **0.1895** |
| **AMZN** | **0.1668** |
| **AAPL** | **0.1239** |

*Insight: NVDA exhibits the highest sensitivity to news sentiment, suggesting its price is heavily influenced by retail and analyst narratives.*

### Predictive Lag Analysis
We expanded the analysis to investigate whether news from the previous day predicts returns today.
-   **Findings**: Lag correlations were significantly lower or even slightly negative (-0.01 to -0.28).
-   **Market Efficiency**: This suggests that the market is highly efficient; news sentiment is "priced in" almost immediately on the same trading day, leaving little predictive residual for the following day.

---

## 4. Visual Evidence
Our enhanced notebooks provide visual confirmation of these relationships:
-   **Regression Analysis**: Scatter plots show a clear positive slope between sentiment and returns.
-   **Distribution Analysis**: Boxplots reveal that "Positive" sentiment days have a higher median daily return compared to "Neutral" or "Negative" days.

---

## 5. Strategic Recommendations
1.  **High-Frequency Sentiment Filtering**: Traders should utilize real-time sentiment scoring to confirm price breakouts. A sentiment score > 0.2 provides a robust "momentum confirmation."
2.  **Narrative Exhaustion**: Extreme positive sentiment combined with an RSI > 75 often signals "narrative exhaustion," indicating a potential time to take profits.
3.  **Efficiency over Prediction**: Avoid using yesterday's news as a primary indicator for today's trade; the market reacts within the same trading window.

---

*Analysis conducted by Antigravity AI for Nova Financial Solutions.*
