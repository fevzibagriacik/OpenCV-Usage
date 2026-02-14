import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
print(img)
#img[200:300, 100:300] = 255, 0, 0 #It fills color on the image
cv2.line(img, (0,0), (img.shape[1],img.shape[0]), (0, 255, 0), 3) #It creates a line from (0,0) to max point
cv2.rectangle(img, (0,0), (300, 300), (0,0,255), cv2.FILLED) #It creates a rectangular
cv2.circle(img, (400,50), 30, (255, 255, 0), 2) #It creates a circle
cv2.putText(img, "OpenCV", (300, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 3)

cv2.imshow("Output", img)
cv2.waitKey(0)