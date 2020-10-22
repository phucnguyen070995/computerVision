from matplotlib import pyplot as plt
from skimage.color import rgb2gray
from scipy.signal import convolve2d, correlate2d
import numpy as np

# load image and convert to grayscale image
im = plt.imread('london.png')
im = rgb2gray(im)

# create kernel
n = 11
kernel = np.ones((n,n))/(n*n)
print(kernel)

# apply correlation
out = correlate2d(im, kernel, mode='same')


# show image
plt.imshow(out, cmap=plt.get_cmap('gray'))
plt.show()

# print size of input and output
print(im.shape)
print(out.shape)