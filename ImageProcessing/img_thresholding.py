# Simple threshold
    #1. Binary
    #2. Binary inverse
    #3. Trunc
    #4. To zero
    #5. Tozero Inverse
# Adaptive thresholding

import cv2

# reading the image
image = cv2.imread(r'.\img\resized.jpg')

thresh1, op_img1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
thresh2, op_img2 = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
thresh3, op_img3 = cv2.threshold(image,127,255,cv2.THRESH_TRUNC)
thresh4, op_img4 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO)
thresh5, op_img5 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)

img =[op_img1,op_img2,op_img3,op_img4,op_img5]

for pic in img:
    cv2.imshow('My pic', pic)
    cv2.waitKeyEx(0)
    cv2.destroyAllWindows()