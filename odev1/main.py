import cv2
import numpy as np

gorsel = cv2.imread("fotograf.jpg", 0)
cv2.imshow("fotograf", gorsel)
cv2.waitKey()

hist = np.zeros(256)
[h, w] = np.shape(gorsel)
for i in range(0, h):
    for j in range(0, w):
        k = gorsel[i, j]
        hist[k] = hist[k] + 1

for i in range(0, 256):
    print(i, "-->", hist[i])
