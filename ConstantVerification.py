#!/home/ocean/anaconda3/bin/python3
from numpy import cos, arccos, sin, arctan, tan, pi, sqrt, e; from numpy import array as ary; import numpy as np; tau = 2*pi
import random as rn
from PowersVerification import *

if __name__=="__main__":
	from matplotlib import pyplot as plt
	x_true_mean = 12
	x_true_vari = 0.12
	c = 3
	y_true_mean = c
	y_true_vari = 0

	sampleLength=900000
	#rn.seed(1954)

	X = distribution(12,0.12)
	Y = distribution(y_true_mean,y_true_vari)

	from scipy import integrate

	EmpiricalCrossTerm = [X.sample()+c for n in range(sampleLength)]	#just the variable  plus the constant itself

	newDist = X+Y
	CalculatedCrossTerm = [newDist.sample() for n in range(sampleLength)]

	y_emp, x_emp, patches = plt.hist(EmpiricalCrossTerm, bins=200, alpha = 0.5, label ="empirically calculated\ndistribution, by\nadding samples\nof X by the constant")
	y_cal, x_cal, patches = plt.hist(CalculatedCrossTerm, bins= 200, alpha = 0.5,label="new distribution\ngenerated using\nthe proper rules")
	plt.legend()
	plt.savefig('addConstant.png')
 #change all methods to ensure that they accommodate for non-zero uncertainty on the mean.
	#What happens with uncertainty on the mean? do I expand it with the chain rule?
#express covariance as something else?