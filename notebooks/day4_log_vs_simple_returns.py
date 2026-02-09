import numpy as np

prices = np.array([100, 105, 102, 110, 120])

# Simple returns
simple_returns = (prices[1:] - prices[:-1]) / prices[:-1]

# Log returns
log_returns = np.log(prices[1:] / prices[:-1])

print("Prices:", prices)

print("\nSimple Returns:")
print(simple_returns)

print("\nLog Returns:")
print(log_returns)

# Compare total return
total_simple_return = (prices[-1] - prices[0]) / prices[0]
total_log_return = np.log(prices[-1] / prices[0])

print("\nTotal Simple Return:", total_simple_return)
print("Total Log Return:", total_log_return)

# Show log return additivity
sum_log_returns = np.sum(log_returns)

print("\nSum of daily log returns:", sum_log_returns)
print("Direct log return from start to end:", total_log_return)

print("\nKey Insight:")
print("Log returns add perfectly over time (sum of log returns = total log return).")

