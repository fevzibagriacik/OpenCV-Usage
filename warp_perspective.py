import cv2
import numpy as np

img = cv2.imread("resources/playing_card.jpg")

width, height = 250, 350
pts1 = np.float32([[496, 114], [685, 154], [441, 385], [632, 423]])
pts2 = np.float32([[0,0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)

img_output = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Output", img)
cv2.imshow("Output Image", img_output)

cv2.waitKey(0)