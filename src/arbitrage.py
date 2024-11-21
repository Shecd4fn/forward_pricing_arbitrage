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
        
def calculate_arbitrage_profit(calculated_forward, market_forward, units=1):
    """
    Calculate arbitrage profit based on the difference between calculated and market forward prices.
    """
    profit = abs(calculated_forward - market_forward) * units
    return profit
