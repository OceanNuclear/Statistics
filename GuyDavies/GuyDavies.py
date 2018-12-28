#!/home/ocean/anaconda3/bin/python3
#Written by Guy Davies, Lecturer at UoB
from numpy import cos, arccos, sin, arctan, tan, pi, sqrt; from numpy import array as ary; import numpy as np; tau = 2*pi
from matplotlib import pyplot as plt
import seaborn
from mpl_toolkits.mplot3d import Axes3D

if __name__ == "__main__":
    x = np.array([80.998, 356.013, 661.657, 1173.228, 1332.492])
    y = [135.22, 616.26, 1153.16, 2047.94, 2327.75]
    yerr = np.array([0.36, 0.58, 0.41, 0.68, 0.56])
    label = ['Ba-133', 'Ba-133', 'Cs-137', 'Co-60', 'Co-60']

    # Plot the data
    fig, ax = plt.subplots()
    ax.errorbar(x, y, yerr=yerr*100.0, fmt='ko', \
                label='Error bars * 100')
    ax.plot(x, 1.75 * x - 6.88, 'r--', label=r'Fit $1.75 x - 6.88$')
    ax.legend(loc=2)
    ax.set_xlabel('Energy (keV)')
    ax.set_ylabel('Centroid channel')
    fig.savefig('data.png')
    # Plot the chisqr surface ...

    m = np.linspace(1.0,2.5,100)
    c = np.linspace(-360,360,100)
    mm ,cc = np.meshgrid(m, c)
    chisqr = np.zeros(mm.shape)
    for i in range(len(x)):
        chisqr += (y[i] - mm * x[i] - cc)**2 / (100.0 *  yerr[i])**2
        chisqr[chisqr > 200] = 200
    fig1, ax1 = plt.subplots()
    ax1.contour(m, c, chisqr, levels=[0,2.3,4.61,6.18,9.21,11.8]+chisqr.min())
    CS = ax1.contourf(m, c, chisqr, 100, cmap='afmhot')
    cbar = fig1.colorbar(CS)
    ax1.set_xlabel('Gradient')
    ax1.set_ylabel('Intercept')
    cbar.ax.set_ylabel(r'$\chi^{2}$')
    ax1.set_title("Error bars * 100")
    fig1.savefig('chisqr_surface.png')

    fig2 = plt.figure()
    ax2 = fig2.gca(projection='3d')
    surf = ax2.plot_surface(mm, cc, chisqr, cmap='afmhot')
    cbar2 = fig2.colorbar(surf)
    cbar2.ax.set_ylabel(r'$\chi^{2}$') 