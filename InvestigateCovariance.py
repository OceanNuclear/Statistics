#!/home/ocean/anaconda3/bin/python3
from numpy import cos, arccos, sin, arctan, tan, pi, sqrt; from numpy import array as ary; import numpy as np; tau = 2*pi
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle


def covariance_matrix(r_matrix, sigma_vector=[1,1]):
    assert len(r_matrix)==len(sigma_vector), "The matrix must be NxN, where N=number of sigma's plugged"
    assert r_matrix.ndim==2, "The matrix must have two dimensions"
    sigmas=np.outer(sigma_vector,sigma_vector)
    return r_matrix*sigmas

def generate_r_matrix(r, dim=2):
    #generates a pearson coefficient matrix
    iden = np.identity(dim)
    off_diag = (np.ones([2,2])-iden)*r
    return iden+off_diag

def get_rect_bounds(means, sigmas): #only works for 2D case
    sigmas=ary(sigmas)*3
    xy = np.subtract(means,sigmas)
    width = sigmas[0] *2
    height= sigmas[1] *2
    return xy, width, height

if __name__=="__main__":
    n_sample=300
    means = [0,0]
    sigma_vec = [1,1]
    for r in np.arange(-1,3,0.2):
        fig, ax = plt.subplots(1)
        r_mat = generate_r_matrix(r)
        cov = covariance_matrix(r_mat)
        list_of_xy = np.random.multivariate_normal(means,cov,size=n_sample)
        ax.scatter(list_of_xy.T[0],list_of_xy.T[1])
        ax.set_title("r="+str(r))
        xy, width, height = get_rect_bounds(means, sigma_vec)
        rect= Rectangle(xy, width, height,linewidth=1,edgecolor='r',facecolor='none')
        ax.add_patch(rect)
        plt.show()
        plt.close()