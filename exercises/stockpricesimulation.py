import numpy as np
import matplotlib.pyplot as plt 

# Set initial stock price
initial_price = 42.76  # as of Sept 26, 2025

# Time horizon: days to January (~3 months, or ~63 trading days)
days_to_jan = 31 + 30 + 31  # Oct, Nov, Dec
T = days_to_jan / 252  # Convert to fraction of trading year

# Assumptions
annual_volatility = 0.55  # High volatility typical of Unity
annual_drift_base = 0.10   # Base case: +10% annual return
annual_drift_bull = 0.35   # Bull case: +35%
annual_drift_bear = -0.15  # Bear case: -15%

# Simulations
n_simulations = 10000
threshold = 55  # Target price

def simulate_price_paths(S0, mu, sigma, T, n=10000):
    Z = np.random.standard_normal(n)
    ST = S0 * np.exp((mu - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
    return ST

# Run simulations
prices_base = simulate_price_paths(initial_price, annual_drift_base, annual_volatility, T, n_simulations)
prices_bull = simulate_price_paths(initial_price, annual_drift_bull, annual_volatility, T, n_simulations)
prices_bear = simulate_price_paths(initial_price, annual_drift_bear, annual_volatility, T, n_simulations)

# Calculate probabilities
prob_base = np.mean(prices_base >= threshold)
prob_bull = np.mean(prices_bull >= threshold)
prob_bear = np.mean(prices_bear >= threshold)

# Plot
plt.figure(figsize=(12, 6))
plt.hist(prices_base, bins=100, alpha=0.6, label=f'Base Case (Prob ≥ $55: {prob_base:.1%})')
plt.hist(prices_bull, bins=100, alpha=0.6, label=f'Bull Case (Prob ≥ $55: {prob_bull:.1%})')
plt.hist(prices_bear, bins=100, alpha=0.6, label=f'Bear Case (Prob ≥ $55: {prob_bear:.1%})')
plt.axvline(threshold, color='red', linestyle='--', label='$55 Target')
plt.title('Unity Stock Price Simulation to January 2025')
plt.xlabel('Simulated Stock Price')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Print raw probabilities
print(f"Base Case Probability ≥ $55: {prob_base:.2%}")
print(f"Bull Case Probability ≥ $55: {prob_bull:.2%}")
print(f"Bear Case Probability ≥ $55: {prob_bear:.2%}")
