import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Fourier.png',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)


rows, cols = img.shape
crow,ccol = int(rows/2) , int(cols/2)

cut_off = 50
fshift[crow-cut_off:crow+cut_off, ccol-cut_off:ccol+cut_off] = 0

f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])


plt.show()