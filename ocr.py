import cv2
import numpy as np
import matplotlib.pyplot as plt
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

####################################
print("A Text Image:\n")
img = cv2.imread('textimg.jpg')

text = pytesseract.image_to_string(img)
print("\n",text)

cv2.imshow("Text Image",img)
cv2.waitKey(0)

#####################################
print("\nImage of a Book Page:\n")
img1 = cv2.imread('book_page.jpg')

print("Text from input image:\n")

text1 = pytesseract.image_to_string(img1)
print("\n",text1)

cv2.imshow("Book Page",img1)
cv2.waitKey(0)

# so now we have to preprocess the image so that the ocr is given only that part of 
#image which contains text
#shrinking the size of image
print("\nText from shrinked image:\n")
imgshrink = cv2.resize(img1,None,fx=0.5,fy=0.5)  #dividing the width and height of image

text2 = pytesseract.image_to_string(imgshrink)
print("\n",text2)

cv2.imshow("Shrinked",imgshrink)
cv2.waitKey(0)

#converting the image to grayscale
print("\nText from grayscale image:\n")
gray = cv2.cvtColor(imgshrink,cv2.COLOR_BGR2GRAY)

text3 = pytesseract.image_to_string(gray)
print("\n",text3)

cv2.imshow("Grayscale",gray)
cv2.waitKey(0)

#applying adaptive threshold since it is affected by the difference in light.
print("\nText from Adaptive Thresholded image\n")
adaptive_threshold = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,85,11)
config = "--psm 3"  #3 is default

text4 = pytesseract.image_to_string(adaptive_threshold, config = config)
print("\n",text4)

cv2.imshow("Adaptive Thresholded Image",adaptive_threshold)
cv2.waitKey(0)