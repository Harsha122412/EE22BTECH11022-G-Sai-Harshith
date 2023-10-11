import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

# Define parameters
mu_values = np.linspace(1, 5, 100)  # Range of means

# For each mean, calculate and plot the CDFs of X and Y at x=µ
for mu in mu_values:
    cdf_X = expon.cdf(mu, scale=mu)
    cdf_Y = expon.cdf(np.floor(mu), scale=mu)

    # Create the plot
    plt.plot(mu, cdf_X, 'bo')  # Plot the CDF of X at the maximum x value
    plt.plot(mu, cdf_Y, 'ro')  # Plot the CDF of Y at the maximum x value

plt.xlabel('μ')
plt.ylabel('CDF')
plt.title('CDFs of X and Y varying μ')
plt.legend(['Y', 'X'])
plt.grid(True)
plt.savefig("../figs/figure.png")
plt.show()

