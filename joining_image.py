import cv2
import numpy as np

img = cv2.imread("resources/demo.png")
img_resize = cv2.resize(img, (300,300))

img_hor = np.hstack((img_resize, img_resize, img_resize)) #A lot of images ordered as horizontal
img_ver = np.vstack((img_resize, img_resize, img_resize)) #A lot of images ordered as vertical

cv2.imshow("Output", img_ver)
cv2.imshow("Output-2", img_hor)

cv2.waitKey(0)