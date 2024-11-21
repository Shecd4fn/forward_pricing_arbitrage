def calculate_hedged_portfolio_value(portfolio_value, forward_contracts, forward_price, market_price):
    """
    Calculate portfolio value after hedging with forward contracts.
    """
    hedge_gain = forward_contracts * (forward_price - market_price)
    return portfolio_value + hedge_gain
