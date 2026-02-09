import numpy as np

n = 1000000

# Generate samples from N(0,1)
samples = np.random.normal(loc=0, scale=1, size=n)

mean = np.mean(samples)
var = np.var(samples)
std = np.std(samples)

print("----- NORMAL DISTRIBUTION SIMULATION -----")
print("Samples:", n)

print("\nEmpirical Results:")
print("Mean:", mean)
print("Variance:", var)
print("Std Dev:", std)

# Z-score example
x = 1.5
z = (x - mean) / std

print("\nZ-Score Example:")
print("If x = 1.5, Z-score =", z)

# Probability estimation using simulation
prob = np.mean(samples > x)

print("\nProbability Estimate:")
print("P(X > 1.5) ≈", prob)

# Finance connection:
# Z-score helps quantify extreme events in returns.
# Example: a -3 sigma move in returns is very rare and signals tail risk.

