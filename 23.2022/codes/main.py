import matplotlib.pyplot as plt
import numpy as np

def plot_function(a):
    x = np.linspace(-10, 10, 1000)
    y = (np.abs(x) <= a).astype(int)  

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(f'|H(f)| vs frequency')
    ax.grid(True)
    ax.set_xticks([-a, a])
    ax.set_xticklabels(['-a', 'a'])
    ax.set_yticks([0, 1])
    plt.savefig("../figs/figure.png")
    plt.show()
a = 5
plot_function(a)
