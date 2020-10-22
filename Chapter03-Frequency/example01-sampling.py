import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Fourier.png',0)
print(img.shape)
sampled_img = img[::16, ::16]
print(sampled_img.shape)

plt.subplot(121),plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(sampled_img, cmap = 'gray')
plt.title('Sampled Image'), plt.xticks([]), plt.yticks([])
plt.show()