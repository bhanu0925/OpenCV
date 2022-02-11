import cv2

# reading the image
image = cv2.imread(filename=r'.\img\nature.jpg')

cv2.imshow('Original', image)
cv2.imshow('Cropped', image[30:150,40:299])

## if the out of bound values are selected, these will be mapped back to the size of the image

cv2.waitKey(0)
cv2.destroyAllWindows()