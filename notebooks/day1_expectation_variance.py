import numpy as np

n = 1000000
rolls = np.random.randint(1, 7, size=n)

emp_mean = np.mean(rolls)
emp_var = np.var(rolls)
emp_std = np.std(rolls)

theo_mean = 3.5
theo_ex2 = (1**2 + 2**2 + 3**2 + 4**2 + 5**2 + 6**2) / 6
theo_var = theo_ex2 - theo_mean**2
theo_std = np.sqrt(theo_var)

print("----- FAIR DIE SIMULATION -----")
print("Rolls:", n)

print("\nEmpirical (Simulation):")
print("Mean:", emp_mean)
print("Variance:", emp_var)
print("Std Dev:", emp_std)

print("\nTheoretical:")
print("Mean:", theo_mean)
print("Variance:", theo_var)
print("Std Dev:", theo_std)

