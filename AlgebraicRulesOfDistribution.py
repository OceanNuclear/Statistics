from numpy import cos, arccos, sin, arctan, tan, pi, sqrt, e; from numpy import array as ary; import numpy as np; tau = 2*pi
import random as rn
from PowersVerification import *

if __name__=="__main__":
	from matplotlib import pyplot as plt
	x_true_mean = 12
	x_true_vari = 0.12

	y_true_mean = 30
	y_true_vari = 0.9

	sampleLength=900000
	#rn.seed(1954)

	X = distribution(12,0.12)
	Y = distribution(y_true_mean,y_true_vari)

	EmpiricalCrossTerm = [X.sample()/Y.sample() for n in range(sampleLength)]

	newDist = X/Y
	CalculatedCrossTerm = [newDist.sample() for n in range(sampleLength)]

	y_emp, x_emp, patches = plt.hist(EmpiricalCrossTerm, bins=200, alpha = 0.5, label ="empirically calculated\ndistribution, by\ndividing samples\nof A with B")
	y_cal, x_cal, patches = plt.hist(CalculatedCrossTerm, bins= 200, alpha = 0.5,label="new distribution\ngenerated using\nthe rules of\n"+r"$\sigma^2(\frac{A}{B})$"+"\n= "+r"$\frac{\sigma^2(A)}{B^2}$ + $\frac{A^2}{B^4} \sigma^2$(B)")
	plt.legend()
	#plt.figtext(0.5, 0.01,"comparisons between the empirically generated distribution\nand the distribution calculated using the correct $\sigma$'s", ha="center")
	#^That line was perfectly functional, but because legend() already explains the graph sufficiently, I've commented it away.
	plt.savefig('X_dist_div_Y_dist_confirmation.png')
