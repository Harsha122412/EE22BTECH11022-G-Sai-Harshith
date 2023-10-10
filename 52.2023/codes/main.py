import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import truncnorm

sigma = 1.0
a, b = 0, np.inf  # Truncated normal between 0 and infinity
x_values = np.linspace(0, 5, 1000)
mus = [0.5, 1.0, 1.5, 2.0]
for mu in mus:
    cdf_X = truncnorm.cdf(x_values, a, b, loc=mu, scale=sigma)
    y_values = np.floor(x_values)
    a_Y, b_Y = np.floor((a - mu) / sigma), np.floor((b - mu) / sigma)
    cdf_Y = truncnorm.cdf(y_values, a_Y, b_Y, loc=mu, scale=sigma)
    plt.plot(x_values, cdf_X, label=f'CDF of X, μ={mu}')
    plt.plot(x_values, cdf_Y, label=f'CDF of Y, μ={mu}')

plt.xlabel('x')
plt.ylabel('CDF')
plt.legend()
plt.title('CDFs of X and Y for varying μ')
plt.savefig("../figs/figure.png")
plt.show()

