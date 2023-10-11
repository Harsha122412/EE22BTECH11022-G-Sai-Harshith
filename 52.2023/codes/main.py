import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon
mu_values = np.linspace(1, 5, 100)  # Range of means
for mu in mu_values:
    cdf_X = expon.cdf(1.5, scale=mu)
    cdf_Y = expon.cdf(np.floor(1.5), scale=mu)
    plt.plot(mu, cdf_X, 'bo')
    plt.plot(mu, cdf_Y, 'ro')  
    
plt.xlabel('μ')
plt.ylabel('CDF at x=1.5')
plt.title('CDFs of X and Y varying μ at x=1.5')
plt.legend(['Y', 'X'])
plt.grid(True)
plt.savefig("../figs/figure.png")
plt.show()
