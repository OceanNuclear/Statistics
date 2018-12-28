#!/home/ocean/anaconda3/bin/python3
from numpy import cos, arccos, sin, arctan, tan, pi, sqrt; from numpy import array as ary; import numpy as np; tau = 2*pi
from matplotlib import pyplot as plt

x = np.linspace(0,5,6)
y = [0.2, 0.2, 0.21, -1.7, -0.4,-0.1]
yerr = np.linspace(0.5,0.5,6)
Sxx = sum(x*x/yerr/yerr)
Sx  = sum(x  /yerr/yerr)
S   = sum(1  /yerr/yerr)
Sxy = sum(x*y/yerr/yerr)
Sy  = sum(  y/yerr/yerr)

Δ = S*Sxx-Sx*Sx
print(Δ)
c = (Sxx*Sy -Sx*Sxy)/Δ
m = (S  *Sxy-Sx*Sy )/Δ
c_var = Sxx/Δ
m_var = S  /Δ
print(m,c,sqrt([m_var,c_var]))