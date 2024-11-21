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
def plot_forward_curve(forward_prices, maturities):
    """Plot forward curve for different maturities."""
    plt.figure(figsize=(10, 6))
    plt.plot(maturities, forward_prices, marker='o')
    plt.xlabel("Time to Maturity (Years)")
    plt.ylabel("Forward Price")
    plt.title("Forward Curve")
    plt.grid()
    plt.show()

def plot_simulation_paths(simulated_prices, steps):
    """Visualize simulated spot price paths."""
    plt.figure(figsize=(10, 6))
    for path in simulated_prices.T:
        plt.plot(range(steps + 1), path, alpha=0.5)
    plt.xlabel("Time Steps")
    plt.ylabel("Spot Price")
    plt.title("Simulated Spot Price Paths")
    plt.grid()
    plt.show()
