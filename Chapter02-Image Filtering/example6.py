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



# Line 2
C = gkern(27, 3)
print(C)
A = convolve2d(C, B, mode='same')
# show image
plt.imshow(A, cmap=plt.get_cmap('gray'))
plt.show()

