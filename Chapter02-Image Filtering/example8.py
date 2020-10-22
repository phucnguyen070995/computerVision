from matplotlib import pyplot as plt
from skimage.color import rgb2gray
from scipy.signal import convolve2d, correlate2d
from tensorflow.python.ops.image_ops_impl import _fspecial_gauss

im = plt.imread('village.png')
im = rgb2gray(im)

result = convolve2d(im, im)
plt.imshow(result, cmap=plt.get_cmap('gray'))
plt.show()

