import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('flower.jpg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)     


f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
plt.title('Image after inversing'), plt.xticks([]), plt.yticks([])


plt.show()