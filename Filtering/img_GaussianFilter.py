import cv2
"""
Averaging filter - boxfilter
gaussian filter
median filter
bilateral filter
"""
# reading the image
image = cv2.imread(filename=r'.\img\nature.jpg')

cv2.imshow('My pic', image)

blur = cv2.GaussianBlur(image,(3,3),5)
cv2.imshow('Gaussian blurring', blur)

cv2.waitKey(0)
cv2.destroyAllWindows()