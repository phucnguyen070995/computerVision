from scipy.signal import convolve2d, correlate2d
import numpy as np

im = np.array([[1, 2, 3, 4, 5], 
               [10, 9, 8, 7, 6],
               [11, 12, 13, 14, 15],
               [21, 22, 23, 24, 25],
               [16, 17, 18, 19, 20]])

kernel = np.array([[0, 1, 0],
                   [0, -2, 0],
                   [2, 0, -1]])

out = convolve2d(im, kernel, mode='same')
print(out)