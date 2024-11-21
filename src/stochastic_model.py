import numpy as np

def simulate_spot_price(S0, mu, sigma, T, steps, simulations):
    """
    Simulates spot prices using Geometric Brownian Motion.
    S(t) = S0 * exp((mu - sigma^2 / 2) * t + sigma * W(t))
    """
    dt = T / steps
    prices = np.zeros((steps + 1, simulations))
    prices[0] = S0

    for t in range(1, steps + 1):
        Z = np.random.standard_normal(simulations)
        prices[t] = prices[t - 1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * Z * np.sqrt(dt))
    
    return prices
