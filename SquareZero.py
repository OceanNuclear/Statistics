from numpy import array as ary; from numpy import log as ln
from numpy import cos, sin, pi, sqrt, exp, arccos;
tau = 2*pi
import numpy as np;
from matplotlib import pyplot as plt

if __name__=='__main__':
    sample_length = 4000
    for mean in np.arange(0, 0.1, 0.2):
        xi = np.random.normal(mean, size=sample_length)
        plt.hist(xi**2, bins=200, alpha=0.5, label="mean={}".format(mean))
        plt.legend()
    plt.show()