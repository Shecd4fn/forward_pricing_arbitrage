def detect_arbitrage(calculated_forward, market_forward):
    """
    Detect arbitrage opportunities by comparing calculated forward price
    with the market forward price.
    """
    if calculated_forward > market_forward:
        return f"Arbitrage Opportunity: Sell Forward at {calculated_forward} and Buy in Market at {market_forward}"
    elif calculated_forward < market_forward:
        return f"Arbitrage Opportunity: Buy Forward at {calculated_forward} and Sell in Market at {market_forward}"
    else:
        return "No Arbitrage Opportunity"
