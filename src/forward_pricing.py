import math

def calculate_forward_price_no_income(S0, r, T):
    """
    Calculate the forward price for an asset with no income.
    F0 = S0 * exp(r * T)
    """
    return S0 * math.exp(r * T)

def calculate_forward_price_with_income(S0, r, T, q):
    """
    Calculate the forward price for an asset with continuous yield q.
    F0 = S0 * exp((r - q) * T)
    """
    return S0 * math.exp((r - q) * T)
