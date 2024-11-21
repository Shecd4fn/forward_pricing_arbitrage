import numpy as np

def perform_sensitivity_analysis(S0, r_values, T_values):
    """
    Perform sensitivity analysis on forward prices for varying interest rates and maturities.
    """
    results = []
    for r in r_values:
        for T in T_values:
            F0 = S0 * np.exp(r * T)
            results.append({"Interest Rate": r, "Maturity": T, "Forward Price": F0})
    return results
