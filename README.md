📈 Stock Market Direction Prediction using Logistic Regression

1. Problem Statement
The objective of this project is to evaluate whether historical market data and technical indicators can be used to predict the next-day stock price direction (Up/Down).

This is treated as a binary classification problem, but with awareness that financial markets are noisy and difficult to predict.

2. Hypothesis
Technical indicators such as momentum, volatility, and volume contain predictive signals that can be used to forecast short-term price direction.

3. Dataset
Source: Yahoo Finance (via yfinance)
Stocks: Large-cap and mid-cap Indian stocks
Time Period: 2010 – 2025
Frequency: Daily (OHLCV)

4. Data Pipeline
The project is structured into three main stages:

4.1 Data Collection
Multi-stock data fetched using yfinance
Cleaned and merged into a single dataset
Stored as Raw_data.csv

4.2 Feature Engineering
Features are computed per ticker using rolling windows and transformations:

Returns: Daily percentage change
Volatility Ratio: Short-term vs long-term volatility
Momentum: 5-day price change
Acceleration: Change in momentum
Volume Spike: Volume relative to rolling average
Position: Price position within recent high-low range
4.3 Target Variable
1 → Next day price is higher
0 → Otherwise

5. Model
Algorithm: Logistic Regression
Class Handling: class_weight="balanced"
Train/Test Split: 80% / 20% (time-based)
Decision Threshold: 0.6 (manually set)

6. Results
Accuracy: ~48%
Model predictions are concentrated near probability = 0.5
The model fails to outperform a random baseline

7. Observations
The model tends to output probabilities close to 0.5, indicating low confidence and weak signal
Logistic Regression struggles to capture patterns in financial time series
Technical indicators alone do not provide sufficient predictive power for direction

8. Failure Analysis
This experiment highlights several key issues:

Low Signal-to-Noise Ratio
Market movements are highly noisy and difficult to model
Linear Model Limitation
Logistic Regression cannot capture non-linear relationships in market data
Feature Weakness
Selected indicators do not contain strong directional information
Evaluation Limitation
Accuracy alone is not sufficient for trading problems

9. Key Insight
The model converges to near-random predictions, indicating a lack of exploitable linear signal in the chosen features for next-day direction prediction.

10. Limitations
No feature scaling applied
No hyperparameter tuning
Multiple tickers combined without encoding
No financial evaluation (PnL, Sharpe ratio, etc.)
Fixed decision threshold without validation

11. Conclusion
This experiment demonstrates that:

Predicting stock direction using simple linear models is extremely challenging
Standard technical indicators do not provide a reliable edge in isolation
Proper evaluation in trading requires more than classification accuracy

🔥 Final Note:
This is not a successful prediction model —
This is a validated failure that reveals the difficulty of extracting signal from financial markets.