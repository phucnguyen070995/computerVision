from matplotlib import pyplot as plt
from skimage.color import rgb2gray

# load image and convert into grayscale
im = plt.imread('london.png')
im = rgb2gray(im)

# show image
plt.imshow(im, cmap=plt.get_cmap('gray'))
plt.show()