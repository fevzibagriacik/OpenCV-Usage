import cv2
import numpy as np

def get_contours(img):
    #RETR_EXTERNAL takes just out edges. CHAIN_APPROX_NONE keeps points of each edge as single
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
    for cnt in contours: #It takes edges of each shape
        area = cv2.contourArea(cnt) #It calculates area of each shapes
        print(area)
        
        if area > 500:
            cv2.drawContours(img_contour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True) #It calculates perimeter of each edge
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True) #It ignores too small contour (how many shapes are there?)
            print(len(approx))
            obj_cor = len(approx)
            x, y, w, h = cv2.boundingRect(approx) 

            if obj_cor == 3: obj_type = "Tri"
            elif obj_cor == 4:
                asp_ratio = w/float(h)
                if asp_ratio > 0.95 and asp_ratio < 1.05: obj_type = "Square"
                else: obj_type = "Rectangular"
            else: obj_type = "None"

            cv2.rectangle(img_contour, (x,y),(x+w,y+h), (0,255,0), 2) #It creates a rectangular from first point to the end point
            cv2.putText(img_contour, obj_type, 
                        (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0), 2)

path = "resources/shapes.jpeg"

img = cv2.resize(cv2.imread(path), (500, 500))
img_contour = img.copy()
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (3,3), 1)
#img_canny = cv2.Canny(img_blur, 30, 100) #We can use this one
ret, img_thresh = cv2.threshold(img_blur, 200, 255, cv2.THRESH_BINARY_INV)
img_blank = np.zeros_like(img)
get_contours(img_thresh)

cv2.imshow("Original Image", img)
cv2.imshow("Gray Image", img_gray)
cv2.imshow("Blur Image", img_blur)
cv2.imshow("Canny Image", img_thresh)
cv2.imshow("Blank Image", img_blank)
cv2.imshow("Countour Image", img_contour)
cv2.waitKey(0)