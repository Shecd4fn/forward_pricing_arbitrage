import matplotlib.pyplot as plt

def plot_forward_prices(spot_prices, forward_prices, market_prices):
    """
    Plot calculated forward prices and market prices for comparison.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(spot_prices, forward_prices, label="Calculated Forward Prices", marker='o')
    plt.plot(spot_prices, market_prices, label="Market Forward Prices", marker='x')
    plt.xlabel("Spot Price")
    plt.ylabel("Forward Price")
    plt.title("Calculated vs Market Forward Prices")
    plt.legend()
    plt.grid()
    plt.show()
