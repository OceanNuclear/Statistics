from numpy import cos, arccos, sin, arctan, tan, pi, sqrt, e; from numpy import array as ary; import numpy as np; tau = 2*pi
import random as rn
from numbers import Number

#Assuming all distributions are independent
class distribution:	#note that I initiate it with sigma square, i.e. vari
	def __init__(self, mu, sigma_sq, sigma_sq_on_mean=0):
		self.mean = mu
		self.vari = sigma_sq
		self.standard_dev = sqrt(sigma_sq)
		self.uncertainy_on_mean=sigma_sq_on_mean
		self.transformed = False
	def sample(self):
			sample = rn.gauss(self.mean, self.standard_dev)
			return sample
	def P(self, x):
		assert isinstance(x, Number)
		s2 = self.vari
		mu = self.mean
		if s2!=0:
			return 1/(sqrt(tau*s2)) * e** ((x-mu)**2/(-2*s2))
		else:
			if x== mu: return np.inf
			else: return 0

	#unary operations
	def __pos__(self): return self
	def __neg__(self): return distribution(-self.mean, self.vari)
	def __pow__(self,n):
		x = self.mean; s2x = self.vari
		new_mean = x**n
		new_vari = (n*x**(n-1))**2 * s2x
		newDist = distribution(new_mean, new_vari)
		return newDist

	#binary operations:
	def __eq__ (self,Y):
		if (self.mean==Y.mean) and (self.vari==Y.vari):
			return True
		else:
			return False
	#def isclose(self, Y):	#if two distributions (inferred from a finite sample size) is 

	#addition and subtraction
	def __add__(self,Y):
		x = self.mean; s2x = self.vari
		if (type(Y)==distribution):
			y = Y.mean; s2y = Y.vari
			new_mean =  x + y
			new_vari = s2x+s2y
		if isinstance(Y, Number): #if it's a scalar number
			new_mean = x+Y
			new_vari = s2x
		newDist = distribution(new_mean, new_vari)
		return newDist
	def __sub__(self,Y):
		newDist = self+ (-Y)	#= add negative version of Y
		return newDist

	#multiplication and division
	def __mul__(self,Y):	#Multiplication is defined below:
		x = self.mean; s2x = self.vari
		if (type(Y)==distribution):
			y = Y.mean; s2y = Y.vari
			new_mean =  x * y
			new_vari = y**2 * s2x + x**2 * s2y
		if isinstance(Y, Number):
			new_mean =  x * Y
			new_vari = s2x*Y**2
		newDist = distribution(new_mean, new_vari)
		return newDist
	def __truediv__(self,Y):
		x = self.mean; s2x = self.vari
		if (type(Y)==distribution):
			y = Y.mean; s2y = Y.vari
			new_mean = x/y
			new_vari = (1/y)**2 * s2x + (x/(-y**2))**2 * s2y
		if isinstance(Y, Number):
			new_mean = x/Y
			new_vari = s2x/(Y**2)
		newDist = distribution(new_mean, new_vari)
		return newDist

def sampleToDist(dataList):
	assert len(np.shape(dataList))==1
	N = len(dataList)
	new_mean = sum(dataList)/N
	new_vari = sum([(i-new_mean)**2 for i in dataList])/(N-1)
	uncertainy_on_mean = new_vari/N
	newDist = distribution(new_mean, new_vari, sigma_sq_on_mean = uncertainy_on_mean)
	return newDist
def sigma(X):
	return X.standard_dev
def sigma_sq(X):
	return X.vari
def mu(X):
	return X.mean

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

	EmpiricalCrossTerm = [X.sample()**3 for n in range(sampleLength)]

	newDist = X**3
	CalculatedCrossTerm = [newDist.sample() for n in range(sampleLength)]
	fig, ax = plt.subplots()

	y_emp, x_emp, patches = ax.hist(EmpiricalCrossTerm, bins=200, alpha = 0.5, label ="empirically calculated\ndistribution, by\nraising samples\nof X to n")
	y_cal, x_cal, patches = ax.hist(CalculatedCrossTerm, bins= 200, alpha = 0.5,label="new distribution\ngenerated using\nthe rules of\n"+r"$\sigma^2(X^n)$"+"= "+r"$n x^{n-1}\sigma^2(X)$")
	#plot probability distribution after transformation:
	ax2 = ax.twinx()
	def f(x):
		return x**3
	def f_inv(x):
		return x**(1/3)
	'''
	Probability density of random variable falling onto u after transformation
		P(u=f(x)) = X.P(x)
		#u = f(x);
		#f_inv(u) = f_inv(f(x) =x
		#f_inv(u) = x
	P(u) = X.P(f_inv(u))
	#That is probably NOT how you'd calculate the PDF.
	#This method requires normalization after transformation, so it's not natural;
	#and it doesn't take into account the stretching thinner /bunching up of the function
	'''
	transformed_PDF = [X.P(f_inv(x_0)) for x_0 in x_cal]
	df_inv = abs(np.diff(f_inv(x_cal)))	#it has to be the absolute value of f^-1'(u). f^-1'(u) must have monotonic sign (f(x) is an invertible (i.e. monotonic continuous) function; so it must always only have +ve or -ve sign.
	scaled_transformed_PDF = df_inv*transformed_PDF[:-1]	#THIS WORKS! It scales down the part of the PDF that gets stretched out more.
	ax2.plot(x_cal[:-1], scaled_transformed_PDF, label = "PDF after\ntransformation")
	ax2.set_ylim(0,max(scaled_transformed_PDF))
	ax.legend()
	#ax2.legend()
	plt.savefig('X_pow_3_with_Px.png')
 #as expected, if X.sample()*X.sample()*X.sample() was used insetad,
 #a wider distribution is obtained instead.
 #Tomorrow: exponentiation and logarithm; exponentiation requires modification of the __pow__ function