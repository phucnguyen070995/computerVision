from matplotlib import pyplot as plt
import numpy as np
import scipy.stats as st
from scipy.signal import convolve2d, correlate2d

def gkern(kernlen=21, nsig=3):
    """Returns a 2D Gaussian kernel."""

    x = np.linspace(-nsig, nsig, kernlen+1)
    kern1d = np.diff(st.norm.cdf(x))
    kern2d = np.outer(kern1d, kern1d)
    return kern2d/kern2d.sum()


# load image
im = plt.imread('village.png')

D = im[:,:,0]
print(D.shape)


B = np.array([[1, 2, 1],
              [0, 0, 0],
              [-1, -2, -1]])


# Line 3
E = np.zeros((3,30))
E[1, 29] = 1
F = convolve2d(D, E, mode='same')

# show image
plt.imshow(F, cmap=plt.get_cmap('gray'))
plt.show()
