import cv2

# reading the image
image = cv2.imread(filename=r'.\img\nature.jpg')
cv2.imshow('My pic', image)

image2 = cv2.imread(filename=r'.\img\nature.jpg',flags=0)
cv2.imshow('My pic2', image2)

cv2.waitKey(0)
cv2.destroyAllWindows()