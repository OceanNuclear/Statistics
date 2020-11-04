import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rn
from numpy import array as ary
from numpy import sqrt
from numpy.linalg import svd, eig, eigvals, inv, pinv

def set_offdiag(mat, triu, inplace=True):
    '''sets the off-diagonal elements of a symmetric matrix when the top triangle's values are given.'''
    triu = ary(triu).flatten()
    indices = ary(np.triu_indices_from(mat, k=1)).T
    if inplace:
        for ij, ord in zip(indices, triu):
            i,j  = ij
            mat[i,j] = ord
            mat[j,i] = ord
        return mat
    else:
        matcopy = mat.copy()
        for ij, ord in zip(indices, triu):
            i,j  = ij
            matcopy[i,j] = ord
            matcopy[j,i] = ord
        return matcopy
    
if __name__=="__main__":
    main_diag = [sqrt(1),.01]
    covar_mat = np.diag(ary(main_diag, dtype=float))
    set_offdiag(covar_mat, [0], inplace=True)
    eigval, eigvec = eig(covar_mat)
    print("eigval=", eigval)
    print("eigvec=\n", eigvec)
    xy = rn.multivariate_normal([0,0], covar_mat, size=1000)
    x, y = xy.T
    ax = plt.subplot()
    ax.scatter(x,y)
    ax.set_aspect(1) # equal aspect ratio
    plt.show()
    plt.clf()