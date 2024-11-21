import pandas as pd
from src.forward_pricing import calculate_forward_price_no_income
from src.arbitrage import detect_arbitrage
from src.visualize import plot_forward_prices

# Load market data
data = pd.read_csv("data/market_data.csv")

# Extract spot prices and market forward prices
spot_prices = data["Spot Price"]
market_forward_prices = data["Market Forward Price"]
r = 0.05  # Example risk-free rate
T = 1  # One year maturity

# Calculate forward prices
calculated_forward_prices = [calculate_forward_price_no_income(S0, r, T) for S0 in spot_prices]

# Detect arbitrage
for calculated, market in zip(calculated_forward_prices, market_forward_prices):
    print(detect_arbitrage(calculated, market))

# Visualize results
plot_forward_prices(spot_prices, calculated_forward_prices, market_forward_prices)
