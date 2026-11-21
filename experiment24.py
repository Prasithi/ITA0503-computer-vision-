import cv2
import numpy as np

image = cv2.imread(r"C:\Users\Dell\Downloads\image.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
blackhat = cv2.morphologyEx(gray_image, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow("Original Image", gray_image)
cv2.imshow("Black Hat Image", blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()
