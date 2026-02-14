import cv2
import numpy as np

img = cv2.imread("resources/demo.png")

kernel = np.ones((5,5), np.uint8)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7, 7), 0) #If kernel size increases, blur of image will increase
img_canny = cv2.Canny(img, 50, 150) #It sets an image which includes edges
img_dialation = cv2.dilate(img_canny, kernel, iterations=3) #It increases thickness of edges of image
img_eroded = cv2.erode(img_canny, kernel, iterations=1) #It decreases thickness of edges of image

cv2.imshow("Output", img_eroded)
cv2.waitKey(0)

