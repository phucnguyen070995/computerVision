import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy.ndimage import gaussian_filter

img = cv2.imread('Fourier.png',0)
print(img.shape)
img_blur = gaussian_filter(img, sigma=15)
sampled_img = img_blur[::16, ::16]
print(sampled_img.shape)

plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(img_blur, cmap = 'gray')
plt.title('Blured Image'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(sampled_img, cmap = 'gray')
plt.title('Sampled Image'), plt.xticks([]), plt.yticks([])
plt.show()