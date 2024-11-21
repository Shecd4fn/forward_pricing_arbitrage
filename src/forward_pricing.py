
import math

def calculate_forward_price_no_income(S0, r, T):
    """Forward price for an asset with no income."""
    return S0 * math.exp(r * T)

def calculate_forward_price_discrete_income(S0, r, T, I):
    """Forward price for an asset with discrete income."""
    return (S0 - I) * math.exp(r * T)

def calculate_forward_price_continuous_yield(S0, r, T, q):
    """Forward price for an asset with continuous yield."""
    return S0 * math.exp((r - q) * T)

def calculate_forward_price_with_storage_cost(S0, r, T, u):
    """Forward price for commodities with storage costs."""
    return S0 * math.exp((r + u) * T)
