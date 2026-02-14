import cv2
import numpy as np

img = cv2.imread("resources/demo.png")
img_resize = cv2.resize(img, (800, 1200)) #It sets width and height of the image
img_cropped = img[100:600, 600:800] #It crops the image with that values

cv2.imshow("Output", img)
cv2.imshow("Output2", img_cropped)
cv2.waitKey(0)

print(img.shape)