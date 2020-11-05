from numpy import cos, arccos, sin, arctan, tan, pi, sqrt, e; from numpy import array as ary; import numpy as np; tau = 2*pi
import random as rn
from PowersVerification import *

def f_inv(x):
	return 1/x

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
	ONE=distribution(1,0)
	EmpiricalCrossTerm = [1/Y.sample() for n in range(sampleLength)]

	newDist = ONE/Y
	CalculatedCrossTerm = [newDist.sample() for n in range(sampleLength)]
	fig, ax = plt.subplots()
	y_emp, x_emp, patches = ax.hist(EmpiricalCrossTerm, bins=200, alpha = 0.5, label ="empirically calculated\ndistribution, by\ninverting samples\nof B")
	y_cal, x_cal, patches = ax.hist(CalculatedCrossTerm, bins= 200, alpha = 0.5,label="new distribution\ngenerated using\nthe rules of\n"+r"$\sigma^2(\frac{1}{B})$"+"\n= "+r"$\frac{1}{B^4} \sigma^2$(B)")
	
	ax2 = ax.twinx()
	transformed_PDF = [Y.P(f_inv(x_0)) for x_0 in x_cal]

	df_inv = abs(np.diff(f_inv(x_cal)))
	scaled_transformed_PDF = df_inv*transformed_PDF[:-1]
	#print(scaled_transformed_PDF)
	ax2.plot(x_cal[:-1], scaled_transformed_PDF, label = "PDF after\ntransformation")
	ax2.set_ylim(0,max(scaled_transformed_PDF))
	ax.legend()
	plt.savefig('Y_dist_inverse_Px.png')